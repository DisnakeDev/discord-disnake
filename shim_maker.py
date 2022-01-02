from importlib import import_module
import inspect
import os
import sys
from typing import Iterable


def fancy_list(prefix: str, to_join: Iterable[str], limit: int = 100, with_brackets: bool = False) -> str:
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


def create_imports(module_name: str) -> str:
    subpckg = import_module(module_name)
    root_module_name = module_name.split(".")[0] + "."
    members = [
        memb for memb, val in inspect.getmembers(subpckg)
        if (
            not memb.startswith("__")
            and memb not in ("TYPE_CHECKING",)
            and not inspect.ismodule(val)  # skip imported modules
            and getattr(val, "__module__", module_name).startswith(root_module_name)  # skip types imported from external modules
        )
    ]
    imports = fancy_list(f"from {module_name} import ", members)

    try:
        public_members = [f"\"{memb}\"" for memb in subpckg.__all__]
    except AttributeError:
        public_members = None

    if public_members:
        new_all = fancy_list("__all__ = ", public_members, with_brackets=True)
        return imports + "\n\n" + new_all + "\n"

    return imports + "\n"


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
            imports = create_imports(f"{pypath}.{fn[:-3]}")
            with open(f"{shim_path}/{fn}", "w", encoding="utf-8") as f:
                f.write(imports)

        elif os.path.isdir(f"{path}/{fn}"):
            os.makedirs(f"{shim_path}/{fn}", exist_ok=True)
            if fn not in os.listdir(shim_path):
                os.mkdir(f"{shim_path}/{fn}")
            shim_folder(f"{path}/{fn}", f"{pypath}.{fn}", f"{shim_path}/{fn}")


def shim(path: str, shim_path: str) -> None:
    os.makedirs("discord", exist_ok=True)
    shim_folder(path, path.rstrip("/").split("/")[-1], shim_path)


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <module path>", file=sys.stderr)
    exit(1)

shim(sys.argv[1], "discord")
