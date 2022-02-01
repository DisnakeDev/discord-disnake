import argparse
import importlib
import importlib.metadata
import pkgutil
import sys
from types import ModuleType

SHIM_SENTINEL = object()


def test_shim_objects(
    base: ModuleType, shim: ModuleType, base_name: str, _recurse_modules: bool = True
) -> int:
    name = base.__name__
    result = 0
    root_package = base_name.split(".", 1)[0]
    for attr in dir(base):
        if attr.startswith("__"):
            continue
        base_attr: object = getattr(base, attr)

        # check the provided attribute is part of the package to check
        # if the attribute isn't from the same module, skip it
        if not getattr(base_attr, "__package__", None) == root_package and not getattr(
            base_attr, "__module__", ""
        ).startswith(base_name):
            continue

        # skip the package as it will never be the same
        if attr == root_package:
            continue

        if isinstance(base_attr, ModuleType):
            if _recurse_modules:
                test_shim_objects(
                    base_attr,
                    getattr(shim, attr),
                    f"{base_name}.{attr}",
                    _recurse_modules=False,
                )
            continue

        shim_attr = getattr(shim, attr, SHIM_SENTINEL)
        if base_attr is not shim_attr:
            print("Attribute mismatch: ", name + "." + attr)
            result = 1

    return result


def test_shim_modules(base: ModuleType, shim: ModuleType, base_name: str) -> int:
    """Test all files that should exist, do exist. For example, collections.abc"""
    result = 0
    # check all shim packages exist
    for pkg in pkgutil.walk_packages(base.__path__):

        try:
            importlib.import_module(f"{shim.__name__}.{pkg.name}")
        except ModuleNotFoundError:
            print(f"Missing module: {shim.__name__}.{pkg.name}")
            result |= 1
        else:
            if pkg.ispkg:
                result |= test_shim_modules(
                    importlib.import_module(f"{base.__name__}.{pkg.name}"),
                    importlib.import_module(f"{shim.__name__}.{pkg.name}"),
                    f"{base_name}.{pkg.name}",
                )

    # check there's no extra modules
    for pkg in pkgutil.walk_packages(shim.__path__):
        try:
            importlib.import_module(f"{base.__name__}.{pkg.name}")
        except ModuleNotFoundError:
            print(f"Extra module: {shim.__name__}.{pkg.name}")
            result |= 1

    return result


def test_shim(base: ModuleType, shim: ModuleType, base_name: str):
    """Run all test methods."""
    res = test_shim_objects(base, shim, base_name)
    res |= test_shim_modules(base, shim, base_name)
    return res


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Test a shim package is identical to the main package."
    )
    parser.add_argument("base", help="Primary module.")
    parser.add_argument("shim", help="Shim module.", nargs="?", default="discord")
    parser.add_argument("packages", help="List of packages to test.", nargs="*", default=["."])

    args = parser.parse_args()

    result = 0
    for pack in args.packages:
        if not pack.startswith("."):
            pack = f".{pack}"

        try:
            base = importlib.import_module(pack, args.base)
            shim = importlib.import_module(pack, args.shim)
        except ModuleNotFoundError as e:
            if e.__traceback__ and e.__traceback__.tb_next:
                frame = e.__traceback__.tb_next
                while True:
                    if frame.tb_next is None:
                        break
                    frame = frame.tb_next
                file = frame.tb_frame.f_code.co_filename
            else:
                file = f"{args.shim}{pack} or {args.base}{pack}"
            print(f"FATAL EXCEPTION encountered while loading {file}: {str(e)}")
            return 1
        result |= test_shim(
            base,
            shim,
            args.base,
        )
    return result


if __name__ == "__main__":
    import time

    start = time.time_ns()
    res = main()
    end = time.time_ns()
    print(f"Took {(end - start) / 1e9} seconds.")
    sys.exit(res)
