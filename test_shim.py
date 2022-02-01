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


def test_file(base: ModuleType, shim: ModuleType) -> List[str]:
    """Test the two files against each other. Any attributes that aren't exposed by the second file are returned as an error."""
    missing_attributes = []
    for attr in dir(base):
        if attr.startswith("_"):
            continue
        if not hasattr(shim, attr):
            logger.error(f"{shim.__name__}.{attr} is missing.")
            missing_attributes.append(attr)
            continue
        if not hasattr(getattr(shim, attr), "__module__"):
            continue
        if getattr(getattr(shim, attr), "__module__") != base.__name__:
            continue
    return missing_attributes


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


def test_module(base: ModuleType, shim: ModuleType, to_skip: List[str] = None):
    """Tests every attribute for every file in the base module."""
    # dot-delimited path to missing attributes
    missing_attributes: Dict[str, List[str]] = {}

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
        if res := test_file(base_module, shim_module):
            missing_attributes[shim_module.__name__] = res
    return missing_attributes


def find_all_submodules(dir: str) -> List[str]:
    """
    Finds all of the submodules in the designated modules and returns a list of them.
    """
    submodules = set()
    for path in glob.iglob(f"{dir}/**/*.py", recursive=True):
        path = path[:-3].replace(os.sep, ".")
        if importlib.util.find_spec(path) is not None:
            submodules.add(path)

    res = sorted([submod[len(dir) : -9] for submod in submodules if submod.endswith("__init__")])
    return res


class Response(TypedDict):
    extra_files: List[str]
    missing_files: List[str]
    missing_attributes: Dict[str, List[str]]


def test_package(base_name: str, shim_name: str) -> Response:
    """
    Imports and recursively tests all submodules of the base and shim package.

    Offloads testing to test_all_replicas
    """
    response: Response = {
        "extra_files": [],
        "missing_files": [],
        "missing_attributes": {},
    }

    base = importlib.import_module(base_name)
    shim = importlib.import_module(shim_name)
    replicas = test_all_replicas(base, shim)
    response["extra_files"] = replicas[0]
    response["missing_files"] = replicas[1]

    response["missing_attributes"].update(
        test_module(base, shim, to_skip=response["missing_files"])
    )
    for module in find_all_submodules(shim_name):
        if not module:
            continue
        base = importlib.import_module(base_name + module)
        shim = importlib.import_module(shim_name + module)

        response["missing_attributes"].update(
            test_module(base, shim, to_skip=response["missing_files"])
        )
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
    if results.get("missing_attributes"):
        for module, attributes in results["missing_attributes"].items():
            logger.error(f"{module} has missing attributes: {', '.join(attributes)}")
    if not any(results.values()):
        logger.info("All tests passed.")
        return 0
    return 1


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="{levelname:<8} -  {message}", style="{")
    import time

    start = time.time_ns()
    res = main()
    end = time.time_ns()
    print(f"Took {(end - start) / 1e9} seconds.")
    sys.exit(res)
