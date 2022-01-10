import inspect
import pathlib
from importlib import import_module
from typing import Iterable, List, Optional, Tuple

import isort

ISORT_CONFIG = pathlib.Path("pyproject.toml")


def fancy_list(
    prefix: str, to_join: Iterable[str], limit: int = 100, with_brackets: bool = False
) -> str:
    as_line = ", ".join(to_join)
    if with_brackets:
        if "," not in as_line:
            as_line += ","
        if len(prefix) + len(as_line) + 2 <= limit:
            return f"{prefix}({as_line})"
    elif len(prefix) + len(as_line) <= limit:
        return prefix + as_line

    if 4 + len(as_line) <= limit:
        return prefix + "(\n    " + as_line + "\n)"

    return prefix + "(\n    " + ",\n    ".join(to_join) + ",\n)"


def sort_imports(imports: str) -> str:
    return isort.api.sort_code_string(imports, file_path=ISORT_CONFIG)


def create_file(module_name: str) -> Tuple[Optional[str], str]:
    """Creates a docstring and imports for a module."""
    subpckg = import_module(module_name)
    root_module_name = module_name.split(".")[0] + "."
    docstring = None
    members = []
    for memb, val in inspect.getmembers(subpckg):
        if memb == "__doc__":
            docstring = val
            continue

        if (
            not memb.startswith("__")
            and memb not in ("TYPE_CHECKING",)
            and (
                not inspect.ismodule(val) or val.__name__.startswith(root_module_name)
            )  # skip imported external modules
            and getattr(val, "__module__", module_name).startswith(
                root_module_name
            )  # skip types imported from external modules
        ):
            members.append(memb)
    code = fancy_list(f"from {module_name} import ", members)

    try:
        public_members = [f'"{memb}"' for memb in subpckg.__all__]
    except AttributeError:
        public_members = None

    if public_members:
        new_all = fancy_list("__all__ = ", public_members, with_brackets=True)
        code += "\n\n" + new_all

    code += f"\n\n# isort: split\nfrom {module_name} import __dict__ as __original_dict__\nlocals().update(__original_dict__)"

    return docstring, sort_imports(code)


def shim_folder(path: pathlib.Path, pypath: str, shim_path: pathlib.Path) -> List[pathlib.Path]:
    modified = []
    for fn in path.iterdir():
        mod = fn.relative_to(path)

        if not (shim_path / mod).parent.exists():
            (shim_path / mod).parent.mkdir(exist_ok=True, parents=True)
            print("Created directory: ", (shim_path / mod))

        if fn.name in ("__init__.py", "__main__.py", "py.typed") and "tasks" != fn.parent.name:
            with open(path / mod, "r", encoding="utf-8") as fr:
                try:
                    with open(shim_path / mod, "r", encoding="utf-8") as fw:
                        if fw.read() == fr.read():
                            continue
                except FileNotFoundError:
                    pass
                fr.seek(0)
                print("Updating file: ", shim_path / mod)
                with open(shim_path / mod, "w", encoding="utf-8") as fw:
                    fw.write(fr.read())
            modified.append(shim_path / mod)

        elif fn.suffix == ".py":
            docstring, imports = create_file(f"{pypath}.{mod.stem}")
            to_write = ""
            if docstring:
                to_write += '"""\n' + docstring.strip() + '\n"""\n\n'
            to_write += imports
            try:
                with open(shim_path / mod) as f:
                    existing = f.read()
            except FileNotFoundError:
                existing = None
            if existing != to_write:
                print("Updating file: ", shim_path / mod)
                with open(shim_path / mod, "w", encoding="utf-8") as f:
                    f.write(to_write)

                modified.append(shim_path / mod)

        elif fn.is_dir():
            (shim_path / mod).mkdir(parents=True, exist_ok=True)
            modified.extend(shim_folder(fn, f"{pypath}.{fn.stem}", shim_path / mod))

    return modified


def shim(path: pathlib.Path, shim_path: pathlib.Path) -> None:
    shim_path.mkdir(parents=True, exist_ok=True)
    return shim_folder(path, path.stem, shim_path)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to the disnake module.")
    parser.add_argument(
        "-s",
        "--shim",
        help="Name of the shim module.",
        default="discord",
    )
    args = parser.parse_args()
    try:
        path = pathlib.Path(args.path)
    except ValueError:
        print(f"Invalid path to package to be shimmed: {args.path}")
        return 2

    path = path.resolve()

    try:
        shim_dir = pathlib.Path(args.shim)
    except ValueError:
        print(f"Invalid path to new package: {args.shim}")
        return 2

    shim_dir = shim_dir.resolve()

    edited = shim(path, shim_dir)
    return edited or None


if __name__ == "__main__":
    import sys

    res = main()
    if res:
        print(len(res), "files modified.")
    else:
        print("No changes were made.")
    sys.exit(bool(res))
