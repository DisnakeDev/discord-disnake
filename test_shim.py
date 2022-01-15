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
) -> List[pathlib.Path]:
    name = base.__name__
    for attr in dir(base):
        if attr.startswith("__"):
            continue
        base_attr: object = getattr(base, attr)
        if not getattr(base_attr, "__package__", None) == base_name.split(".", 1)[
            0
        ] and not getattr(base_attr, "__module__", "").startswith(base_name):
            continue

        if attr == base_name.split(".", 1)[0]:
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
        if not base_attr is shim_attr:
            print("Attribute mismatch: ", name + "." + attr)
        else:
            pass
            # print(attr, " is the same")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Test a shim package is identical to the main package."
    )
    parser.add_argument("base", help="Primary module.")
    parser.add_argument("shim", help="Shim module.", nargs="?", default="discord")
    parser.add_argument("packages", help="List of packages to test.", nargs="*", default=["."])

    args = parser.parse_args()

    for pack in args.packages:
        if not pack.startswith("."):
            pack = f".{pack}"
        test_shim(
            importlib.import_module(pack, args.base),
            importlib.import_module(pack, args.shim),
            args.base,
        )


if __name__ == "__main__":
    import time

    start = time.time_ns()
    res = main()
    end = time.time_ns()
    print(f"Took {(end - start) / 1e9} seconds.")
    sys.exit()
