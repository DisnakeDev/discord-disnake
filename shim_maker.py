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
from typing import List

import isort

ISORT_CONFIG = pathlib.Path("pyproject.toml")


def find_packages(dir: str, package: str = None) -> List[str]:
    """
    Finds all of the submodules in the designated modules and returns a list of them.
    """
    submodules = set()
    package = package or dir
    for path in glob.iglob(f"{dir}/**/*.py", recursive=True):
        path = path[len(dir) : -3].replace(os.sep, ".")
        if importlib.util.find_spec(path, package) is not None:
            submodules.add(path)

    return sorted([submod[:-9] for submod in submodules if submod.endswith("__init__")])


def _shim_code(code: ModuleType) -> str:
    """Provided code, returns the shimmed version of it."""
    shim = ""
    if code.__doc__:
        shim += f'"""{code.__doc__}"""\n'

    imports = set()

    # add all non-private attributes
    def _filter_members(member):
        return hasattr(member, "__module__") and member.__module__ == code.__name__

    for name, _ in inspect.getmembers(code, predicate=_filter_members):
        if name.startswith("_"):
            continue
        imports.add(name)

    if hasattr(code, "__all__"):
        imports.update(code.__all__)

        shim += "__all__ = (\n"
        shim += textwrap.indent(
            "\n".join([f'"{member}",' for member in sorted(code.__all__)]), "    "
        )
        shim += "\n)\n\n"

    shim += f"from {code.__name__} import {', '.join(sorted(imports))}\n"

    shim += textwrap.dedent(
        f"""
        # isort: split
        from {code.__name__} import __dict__ as __original_dict__

        locals().update({{k: v for k, v in __original_dict__.items() if k not in ("__file__", "__path__", "__name__", "__package__", "__loader__")}})
        del __original_dict__
        """
    )
    shim = isort.api.sort_code_string(shim, file_path=ISORT_CONFIG)
    return shim


def _shim_module_type(
    base_module: ModuleType, shim_module: str, *, original_shim: pathlib.Path = None
):
    """
    Shim a module into the other location.
    """
    if not base_module.__file__:
        raise RuntimeError(f"{base_module} does not have a __file__ attribute")
    # convert the shim_module to a path
    shim_path = shim_module.replace(".", os.sep)
    # handle __init__
    if base_module.__file__.endswith("__init__.py"):
        shim_path += os.sep + "__init__.py"
    else:
        shim_path += ".py"

    if not os.path.exists(os.path.dirname(shim_path)):
        os.makedirs(os.path.dirname(shim_path))

    # actually shim the file
    code = _shim_code(base_module)
    with open(shim_path, "w") as f:
        f.write(code)

    if os.path.exists(py_typed := os.path.dirname(base_module.__file__) + os.sep + "py.typed"):
        shutil.copyfile(py_typed, os.path.dirname(shim_path) + os.sep + "py.typed")


def shim_module(base_name, shim_name, module_name, original_shim: pathlib.Path = None):
    """Shim a module and all of its submodules."""
    base = importlib.import_module(module_name or base_name, base_name)
    _shim_module_type(base, shim_name + module_name, original_shim=original_shim)
    for module in pkgutil.iter_modules(base.__path__):
        if module.ispkg:
            continue
        submodule_name = module_name + "." + module.name
        _shim_module_type(
            importlib.import_module(base_name + submodule_name),
            shim_name + submodule_name,
            original_shim=original_shim and original_shim / f"{module.name}.py",
        )


def main(base_name: str, shim_name: str):
    base = importlib.import_module(base_name)
    if not base.__file__:
        raise RuntimeError(f"{base_name} does not have a __file__ attribute")
    base_dir = os.path.dirname(base.__file__)
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
