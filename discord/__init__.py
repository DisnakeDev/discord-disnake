import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import os
import sys
import types

MAIN_PACKAGE = "disnake"


def _find_file(fullname, path=None):
    """Give a fullname, find the file on disk."""
    # this is hacky but it probably works?
    # i couldn't figure out a better way to do this
    # and i don't want to lie in my comments
    # so i'm sorry
    if path is None:
        path = sys.path
    for pth in path:
        item = os.path.join(pth, fullname.replace(".", os.sep))
        if os.path.exists(item):
            return os.path.join(item, "__init__.py")
        if os.path.exists(item + ".py"):
            return item
    raise ImportError("No module named {}".format(fullname))


class MainLoader(importlib.abc.ExecutionLoader):
    def get_filename(self, fullname):

        spec = importlib.util.find_spec(fullname)
        if not spec or not spec.origin:
            raise ImportError

        return spec.origin

    def get_source(self, fullname):
        if file := self.get_filename(fullname):
            with open(file, "r") as f:
                return f.read()
        raise ImportError


class Loader(importlib.abc.SourceLoader, importlib.abc.Loader):
    def get_data(self, path):
        with open(path, "r") as f:
            return f.read()

    def get_filename(self, fullname):

        return _find_file(fullname)

    def get_source(self, fullname):
        if file := self.get_filename(fullname):
            with open(file, "r") as f:
                return f.read()
        raise ImportError

    def create_module(self, spec):
        return None

    def exec_module(self, module: types.ModuleType) -> None:
        """
        Executes the module.
        """
        # Get the path to the module
        path = self.get_filename(module.__spec__.name)
        if not path:
            raise RuntimeError("Could not find module")
        # Execute the module
        with open(path, "r") as f:
            code = compile(f.read(), path, "exec")
        exec(code, module.__dict__)

        # add the parent module to the global dictionary and
        # force the module to be an attribute
        if "." not in module.__spec__.name:
            return
        shimparent, name = module.__spec__.name.rsplit(".", 1)
        parent = shimparent.replace(__name__, MAIN_PACKAGE, 1)
        if sys.modules.get(shimparent) is not None:
            if parent not in sys.modules:
                importlib.import_module(parent)
            # extremely hacky
            ogparentmodule = sys.modules[parent]
            setattr(ogparentmodule, name, module)


class DiscordFinder(importlib.machinery.PathFinder):
    @classmethod
    def find_spec(cls, fullname: str, path=None, target=None):
        """Try to find a spec for 'fullname' on sys.path or 'path'.
        The search is based on sys.path_hooks and sys.path_importer_cache.
        """
        if not fullname.startswith(__name__ + "."):
            return None
        ogname = fullname
        fullname = fullname.replace(__name__, MAIN_PACKAGE, 1)

        # implement a custom loader for __main__
        if fullname.endswith("__main__"):
            return importlib.util.spec_from_loader(fullname, MainLoader())
        if fullname in sys.modules:
            return importlib.util.find_spec(fullname)

        spec = importlib.machinery.PathFinder.find_spec(fullname, path=path)
        if spec:
            return spec

        # attempt with an unshimmed package
        spec = importlib.util.spec_from_loader(ogname, Loader())
        return spec


def add_import_hook():
    sys.meta_path.append(DiscordFinder)
    sys.modules[__name__] = sys.modules.get(MAIN_PACKAGE) or importlib.import_module(MAIN_PACKAGE)


add_import_hook()
