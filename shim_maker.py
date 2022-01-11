import inspect
import os
import pathlib
import sys
from importlib import import_module
from typing import Iterable, List, Optional, Tuple
import isort

ISORT_CONFIG = pathlib.Path(".isort.cfg")


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


def create_file(module_name: str) -> Tuple[str, str]:
    """Creates a docstring and imports for a module."""
    subpckg = import_module(module_name)
    root_module_name = module_name.split(".")[0] + "."
    docstring = None
    members = []
    for memb, val in inspect.getmembers(subpckg):
        if memb == "__doc__":
            docstring = val

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

    imports = fancy_list(f"from {module_name} import ", members)

    imports += f"\nfrom {module_name} import __dict__ as __original_dict__\n\n"

    try:
        public_members = [f'"{memb}"' for memb in subpckg.__all__]
    except AttributeError:
        public_members = None

    if public_members:
        new_all = fancy_list("__all__ = ", public_members, with_brackets=True)
        imports +=  new_all + "\n\n"

    imports += "locals().update(__original_dict__)\n\ndel __original_dict__\n"

    return docstring, sort_imports(imports).strip()


def shim_folder(path: str, pypath: str, shim_path: str) -> None:
    for fn in os.listdir(path):
        if fn in ("__init__.py", "__main__.py", "py.typed"):
            with open(f"{path}/{fn}", "r", encoding="utf-8") as f:
                content = f.read()
            with open(f"{shim_path}/{fn}", "w", encoding="utf-8") as f:
                f.write(content)

        elif fn.startswith("__"):
            pass

        elif fn.endswith(".py"):

            docstring, imports = create_file(f"{pypath}.{fn[:-3]}")

            with open(f"{shim_path}/{fn}", "w", encoding="utf-8") as f:
                if docstring:
                    f.write('"""\n' + docstring.strip() + '\n"""\n\n')
                f.write(imports + "\n")

        elif os.path.isdir(f"{path}/{fn}"):
            os.makedirs(f"{shim_path}/{fn}", exist_ok=True)
            shim_folder(f"{path}/{fn}", f"{pypath}.{fn}", f"{shim_path}/{fn}")


def shim(path: str, shim_path: str) -> None:
    os.makedirs("discord", exist_ok=True)
    shim_folder(path, path.rstrip("/").split("/")[-1], shim_path)


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <module path>", file=sys.stderr)
    exit(1)

shim(sys.argv[1], "discord")
