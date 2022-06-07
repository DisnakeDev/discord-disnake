import argparse
import glob
import importlib
import importlib.util
import inspect
import os
import pathlib
import pkgutil
import shutil
import sys
import textwrap
from types import ModuleType
from typing import Any, List, Optional

import isort

ISORT_CONFIG = pathlib.Path("pyproject.toml")

BLACKLIST = ("disnake.types",)


def find_packages(dir: str, package: Optional[str] = None) -> List[str]:
    """
    Finds all of the submodules in the designated modules and returns a list of them.

    Parameters
    ----------
    dir : str
        The directory to search for packages.
    package : str, optional
        The package to search for submodules, defaults to dir.
    """
    submodules = set()
    package = package or dir
    for path in glob.iglob(f"{dir}/**/__init__.py", recursive=True):
        path = path[len(dir) : -3].replace(os.sep, ".")
        if importlib.util.find_spec(path, package) is not None:
            # 9 is the number of characters in '__init__'
            submodules.add(path[:-9])

    return sorted(submodules)


def _type_shim_code(code: ModuleType, is_init: bool = False) -> str:
    """Provided code, returns a type-stub version of it."""
    shim = ""
    if code.__doc__:
        shim += f'"""{code.__doc__}"""\n'

    imports = set()

    # add all non-private attributes
    def _filter_members(member):
        if is_init:
            return inspect.ismodule(member) and member.__name__.startswith(code.__name__)
        else:
            return hasattr(member, "__module__") and member.__module__ == code.__name__

    for name, member in inspect.getmembers(code, predicate=_filter_members):
        if name.startswith("_"):
            continue
        if is_init:
            imports.add(member.__name__[len(code.__name__) + 1 :])
        else:
            imports.add(name)

    if hasattr(code, "__all__") and not is_init:
        imports.update(code.__all__)

        if len(code.__all__) > 1:
            shim += "__all__ = (\n"
            shim += textwrap.indent(
                "\n".join([f'"{member}",' for member in sorted(code.__all__)]), "    "
            )
            shim += "\n)\n\n"
        elif len(code.__all__) == 1:
            shim += "__all__ = (" + f'"{code.__all__[0]}",' + ")\n\n"
        else:
            shim += "__all__ = ()\n\n"

    if is_init:
        shim += f"from {code.__name__} import *\n"
        for mod in imports:
            shim += f"from .{mod} import *\n"
    else:
        shim += f"from {code.__name__} import {', '.join(sorted(imports))}\n"

    shim = isort.api.sort_code_string(shim, file_path=ISORT_CONFIG)
    return shim.strip() + "\n"


def _shim_module_type(
    base_module: ModuleType, shim_module: str, *, original_shim: Optional[pathlib.Path] = None
):
    """
    Shim a module into the other location.
    """
    if not base_module.__file__:
        raise RuntimeError(f"{base_module}'s __file__ attribute is not set")
    # convert the shim_module to a path
    shim_path = shim_module.replace(".", os.sep)
    # handle __init__
    if base_module.__file__.endswith("__init__.py"):
        shim_path += os.sep + "__init__.pyi"
        is_init = True
    else:
        shim_path += ".pyi"
        is_init = False

    if not os.path.exists(os.path.dirname(shim_path)):
        os.makedirs(os.path.dirname(shim_path), exist_ok=True)

    # actually shim the file
    code = _type_shim_code(base_module, is_init=is_init)
    with open(shim_path, "w", encoding="utf8") as f:
        f.write(code)

    if os.path.exists(py_typed := os.path.dirname(base_module.__file__) + os.sep + "py.typed"):
        shutil.copyfile(py_typed, os.path.dirname(shim_path) + os.sep + "py.typed")


def shim_module(
    base_name: str, shim_name: str, module_name: str, original_shim: Optional[pathlib.Path] = None
):
    """Shim a module and all of its submodules."""
    base = importlib.import_module(module_name or base_name, base_name)
    _shim_module_type(base, shim_name + module_name, original_shim=original_shim)
    for module in pkgutil.iter_modules(base.__path__):
        if module.ispkg:
            continue
        submodule_name = module_name + "." + module.name
        if (base_name + submodule_name).startswith(BLACKLIST):
            continue
        _shim_module_type(
            importlib.import_module(base_name + submodule_name),
            shim_name + submodule_name,
            original_shim=original_shim and original_shim / f"{module.name}.py",
        )


def main(base_name: str, shim_name: str) -> Any:
    base = importlib.import_module(base_name)
    if not base.__file__:
        raise RuntimeError(f"{base_name}'s __file__ attribute is not set")
    base_dir = os.path.dirname(base.__file__)
    # i don't care enough at the moment to do this the right way
    original_init = os.path.join(shim_name, "__init__.py")

    with open(original_init, "rb") as f:
        original_init_code = f.read()
    # delete the entire shim to remove files that should no longer be shimmed
    shutil.rmtree(shim_name)
    os.makedirs(shim_name)
    # rewrite the original init code
    with open(original_init, "wb") as f:
        f.write(original_init_code)

    packages = find_packages(base_dir, base_name)
    for package in packages:
        shim_module(base_name, shim_name, package)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create a shim for a module.")
    parser.add_argument("module", help="The module to create a shim for.")
    parser.add_argument(
        "-o", "--output", help="The output module to write the shim to.", default="discord"
    )

    args = parser.parse_args()

    sys.exit(main(args.module, args.output))
