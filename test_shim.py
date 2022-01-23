import argparse
import importlib
import importlib.metadata
import pathlib
import sys
from types import ModuleType
from typing import List

SHIM_SENTINEL = object()


def test_shim(
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
            # print('uhm',base_attr,base,attr)
            continue

        # skip the package as it will never be the same
        if attr == root_package:
            continue

        if isinstance(base_attr, ModuleType):
            if _recurse_modules:
                test_shim(
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
        result |= test_shim(
            importlib.import_module(pack, args.base),
            importlib.import_module(pack, args.shim),
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
