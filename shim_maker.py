import os
from importlib import import_module
from typing import Iterable


def fancy_list(prefix: str, to_join: Iterable[str], limit: int = 100, with_brackets: bool = False):
    as_line = ", ".join(to_join)
    if len(prefix) + len(as_line) + int(with_brackets) * 2 <= limit:
        return prefix + as_line if not with_brackets else f"{prefix}({as_line})"

    if 4 + len(as_line) <= limit:
        return prefix + "(\n    " + as_line + "\n)"

    return prefix + "(\n    " + ",\n    ".join(to_join) + ",\n)"


def create_imports(module_name: str) -> str:
    subpckg = import_module(module_name)
    members = [memb for memb in dir(subpckg) if not memb.startswith("__")]
    imports = fancy_list(f"from {module_name} import ", members)

    try:
        public_members = [f"\"{memb}\"" for memb in subpckg.__all__]
    except AttributeError:
        public_members = None

    if public_members:
        new_all = fancy_list("__all__ = ", public_members, with_brackets=True)
        return imports + "\n\n" + new_all + "\n"

    return imports + "\n"


def shim_folder(path, shim_path):
    pypath = path.strip("/").replace("/", ".")
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
            if fn not in os.listdir(shim_path):
                os.mkdir(f"{shim_path}/{fn}")
            shim_folder(f"{path}/{fn}", f"{shim_path}/{fn}")


try:
    os.mkdir("discord")
except Exception:
    pass

shim_folder('disnake', 'discord')
