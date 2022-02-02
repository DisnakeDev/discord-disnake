"""
Test that the second provided package is a near-perfect shim of the first package.

This means that:
- All modules in the shim package are in the main package.
- All modules in the main package are in the shim package.
- Every attribute is exported at minimum, where it is defined in the main package.
- No additional files exist in the shim package.

"""
import argparse
import glob
import importlib
import importlib.util
import logging
import os
import pkgutil
import sys
from types import ModuleType
from typing import Dict, List, Set, Tuple, TypedDict

logger = logging.getLogger(__name__)


class AttributeErrors(TypedDict):
    missing_attributes: List[str]
    mismatching_attributes: List[str]


class Response(TypedDict):
    extra_files: List[str]
    missing_files: List[str]
    attributes: Dict[str, AttributeErrors]


def test_file(base: ModuleType, shim: ModuleType) -> AttributeErrors:
    """Test the two files against each other. Any attributes that aren't exposed by the second file are returned as an error."""
    missing_attributes = []
    mismatching_attributes = []
    for attr in dir(base):
        if attr.startswith("_"):
            continue
        if not hasattr(shim, attr):
            logger.error(f"{shim.__name__}.{attr} is missing.")
            missing_attributes.append(attr)
            continue

        shim_attr = getattr(shim, attr)
        if not hasattr(shim_attr, "__module__"):
            continue
        if getattr(shim_attr, "__module__") != base.__name__:
            continue
        if getattr(base, attr) is shim_attr:
            continue
        logger.error(f"{shim.__name__}.{attr} is not the same as {base.__name__}.{attr}")
        mismatching_attributes.append(attr)
    return {
        "missing_attributes": missing_attributes,
        "mismatching_attributes": mismatching_attributes,
    }


def test_all_replicas(base: ModuleType, shim: ModuleType) -> Tuple[List[str], List[str]]:
    """
    Checks every module has a counterpart.

    Returns a Tuple of modules that should exist and modules that shouldn't exist, if any
    """
    extra_files = []
    missing_files = []
    sub_packages: Set[str] = set()
    for pkg in pkgutil.walk_packages(base.__path__):
        if importlib.util.find_spec(f"{shim.__name__}.{pkg.name}") is None:
            missing_files.append(f"{shim.__name__}.{pkg.name}")
            continue
        if pkg.ispkg:
            sub_packages.add(pkg.name)

    for pkg in pkgutil.walk_packages(shim.__path__):
        if importlib.util.find_spec(f"{base.__name__}.{pkg.name}") is None:
            extra_files.append(f"{base.__name__}.{pkg.name}")
            continue
        if pkg.ispkg:
            sub_packages.add(pkg.name)

    for pkg_name in sorted(sub_packages):
        sub_base = importlib.import_module(f"{base.__name__}.{pkg_name}")
        sub_shim = importlib.import_module(f"{shim.__name__}.{pkg_name}")
        result = test_all_replicas(sub_base, sub_shim)
        extra_files.extend(result[0])
        missing_files.extend(result[1])

    extra_files = sorted(set(extra_files))
    missing_files = sorted(set(missing_files))

    return (extra_files, missing_files)


def test_module(
    base: ModuleType, shim: ModuleType, to_skip: List[str] = None
) -> Dict[str, AttributeErrors]:
    """Tests every attribute for every file in the base module."""
    # dot-delimited path to missing attributes
    results: Dict[str, AttributeErrors] = {}

    if to_skip is None:
        to_skip = []

    for module in pkgutil.walk_packages(base.__path__):
        if f"{shim.__name__}.{module.name}" in to_skip:
            logger.info(f"SKIPPING checking attributes in {shim.__name__}.{module.name}")
            continue
        base_module = importlib.import_module(f"{base.__name__}.{module.name}")
        shim_module = importlib.import_module(f"{shim.__name__}.{module.name}")
        # if module.ispkg:
        #     missing_attributes.update(test_module(base_module, shim_module,to_skip=to_skip))
        #     continue
        if (res := test_file(base_module, shim_module)) and any(res.values()):
            results[shim_module.__name__] = res

    return results


def find_all_submodules(dir: str, package: str = None) -> List[str]:
    """
    Finds all of the submodules in the designated modules and returns a list of them.
    """
    submodules = set()
    package = package or dir
    for path in glob.iglob(f"{dir}/**/*.py", recursive=True):
        path = path[len(dir) : -3].replace(os.sep, ".")
        if importlib.util.find_spec(path, package) is not None:
            submodules.add(path)

    return sorted([submod[:-9] for submod in submodules if submod.endswith("__init__")])


def test_package(base_name: str, shim_name: str) -> Response:
    """
    Imports and recursively tests all submodules of the base and shim package.

    Offloads testing to test_all_replicas
    """
    response: Response = {
        "extra_files": [],
        "missing_files": [],
        "attributes": {},
    }

    base = importlib.import_module(base_name)
    shim = importlib.import_module(shim_name)
    replicas = test_all_replicas(base, shim)
    response["extra_files"] = replicas[0]
    response["missing_files"] = replicas[1]

    response["attributes"].update(test_module(base, shim, to_skip=response["missing_files"]))
    for module in find_all_submodules(shim_name):
        if not module:
            continue
        base = importlib.import_module(base_name + module)
        shim = importlib.import_module(shim_name + module)

        response["attributes"].update(test_module(base, shim, to_skip=response["missing_files"]))
    return response


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Test a shim package is identical to the main package."
    )
    parser.add_argument("base", help="Primary module.")
    parser.add_argument("shim", help="Shim module.", nargs="?", default="discord")

    args = parser.parse_args()

    results = test_package(args.base, args.shim)
    if results.get("extra_files"):
        logger.warning(f"Extra modules: {results['extra_files']}")
    if results.get("missing_files"):
        logger.error(f"Missing modules: {', '.join(results['missing_files'])}")
    if results.get("attributes"):
        for module, attributes in results["attributes"].items():
            if attributes["missing_attributes"]:
                logger.error(
                    f"{module} has missing attributes: {', '.join(attributes['missing_attributes'])}"
                )
            if attributes["mismatching_attributes"]:
                logger.error(
                    f"{module} has mismatching attributes: {', '.join(attributes['mismatching_attributes'])}"
                )

    if not any(results.values()):
        logger.info("All tests passed.")
        return 0
    return 1


if __name__ == "__main__":
    try:
        import coloredlogs
    except ModuleNotFoundError:
        logging.basicConfig(level=logging.DEBUG, format="{levelname:<8} -  {message}", style="{")
    else:
        coloredlogs.install(level="DEBUG", fmt="{levelname:<8} -  {message}", style="{")

    import time

    start = time.time_ns()
    res = main()
    end = time.time_ns()
    print(f"Took {(end - start) / 1e9} seconds.")
    sys.exit(res)
