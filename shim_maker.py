import importlib
import inspect
import pathlib
import sys
import textwrap
import types
from importlib import import_module
from typing import Iterable, List, Optional, Tuple

import isort

ISORT_CONFIG = pathlib.Path("pyproject.toml")


def fancy_list(prefix: str, to_join: Iterable[str]) -> str:
    prefix = prefix.rstrip()
    if not len(to_join):
        return ""
    if len(to_join) > 1:
        return prefix + " (\n    " + ",\n    ".join(to_join) + ",\n)"
    return prefix + " (" + f",\n{' ' * 4}".join(to_join) + ",)"


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

    code = fancy_list(
        f"from typing import TYPE_CHECKING\nif TYPE_CHECKING:\n{' ' * 4}from {module_name} import ",
        members,
    )

    try:
        public_members = [f'"{memb}"' for memb in subpckg.__all__]
    except AttributeError:
        public_members = None

    if public_members:
        new_all = fancy_list("__all__ = ", public_members)
        code += "\n\n" + new_all
    code += "\n"
    code += f"\n# isort: split\nfrom {module_name} import __dict__ as __original_dict__\nlocals().update(__original_dict__)"
    code = code.strip()

    return docstring, sort_imports(code)


def shim_folder(path: pathlib.Path, pypath: str, shim_path: pathlib.Path) -> List[pathlib.Path]:
    modified = []
    for fn in path.iterdir():
        shim_mod = shim_path / fn.relative_to(path)

        if not (shim_mod).parent.exists():
            (shim_mod).parent.mkdir(exist_ok=True, parents=True)
            print("Created directory: ", (shim_mod))

        if fn.name in ("__init__.py", "__main__.py", "py.typed") and "tasks" != fn.parent.name:
            if fn.name == "__init__.py" and fn.parent.name == pypath.split(".", 1)[0]:
                # we will take care of this file later
                continue
            data = sort_imports(fn.read_text(encoding="utf-8"))
            if shim_mod.is_file() and data == shim_mod.read_text(encoding="utf-8"):
                continue
            print("Updating file: ", shim_mod)
            shim_mod.write_text(data, encoding="utf-8")
            modified.append(shim_mod)

        elif fn.suffix == ".py":
            if fn.stem == "__init__":
                mod_path = pypath
            else:
                mod_path = f"{pypath}.{fn.stem}"
            docstring, imports = create_file(mod_path)

            to_write = ""
            if docstring:
                to_write += '"""\n' + docstring.strip() + '\n"""\n\n'
            to_write += imports

            if shim_mod.is_file():
                existing = shim_mod.read_text(encoding="utf-8")
            else:
                existing = None

            if existing != to_write:
                print("Updating file: ", shim_mod)
                shim_mod.write_text(to_write, encoding="utf-8")
                modified.append(shim_mod)

        elif fn.is_dir():
            (shim_mod).mkdir(parents=True, exist_ok=True)
            modified.extend(shim_folder(fn, f"{pypath}.{fn.stem}", shim_mod))

    return modified


def shim_init(path: pathlib.Path, shim_path: pathlib.Path) -> List[pathlib.Path]:

    init = shim_path / "__init__.py"
    if init.is_file():
        existing = init.read_text(encoding="utf-8")
    else:
        existing = None

    data = sort_imports((path / "__init__.py").read_text(encoding="utf-8"))
    init.write_text(data)

    importlib.invalidate_caches()
    base = importlib.import_module(path.stem)
    shim = importlib.import_module(shim_path.stem)
    modules = set()

    for mem in dir(base):
        base_attr = getattr(base, mem)
        if not isinstance(base_attr, types.ModuleType):
            continue
        shim_attr = getattr(shim, mem, None)
        if shim_attr:
            continue

        modules.add(mem)

    data += "\n"
    data += textwrap.dedent(
        f"""
    # Because the main library lazy loads some files, its important to re-export them here.
    # However, because they are lazily loaded, we don't want them showing up on intellisense
    # so should not be reaching when typechecking.
    from typing import TYPE_CHECKING
    """
    )

    code = fancy_list(f"if not TYPE_CHECKING:\n    from {path.stem} import ", modules)
    txt = sort_imports(data + "\n" + code + "\n")

    if existing != txt:
        print("Updating file: ", init)

    with open(init, "w") as f:
        f.write(txt)

    if existing == txt:
        return []

    return [init]


def shim(path: pathlib.Path, shim_path: pathlib.Path) -> List[pathlib.Path]:
    shim_path.mkdir(parents=True, exist_ok=True)
    res = shim_folder(path, path.stem, shim_path)

    # reshim __init__.py
    res.extend(shim_init(path, shim_path))
    return res


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to the disnake module.")
    parser.add_argument(
        "shim",
        help="Name of the shim module.",
        nargs="?",
        default="discord",
    )
    parser.add_argument("--files", help=argparse.SUPPRESS, dest="files", nargs="*", default=None)
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
    if args.files:
        for edited_file in edited:
            if str(edited_file) in args.files:
                args.files.remove(str(edited_file))

        if args.files:
            print(f"The following files were not found: {','.join(args.files)}")
            return 1

    return edited or 0


if __name__ == "__main__":
    import sys

    res = main()
    if res:
        print(len(res), "files modified.")
    else:
        print("No changes were made.")

    sys.exit(bool(res))
