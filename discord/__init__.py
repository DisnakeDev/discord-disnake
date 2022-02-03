import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import os
import sys

MAIN_PACKAGE = "disnake"


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


class DiscordFinder(importlib.machinery.PathFinder):
    @classmethod
    def find_spec(cls, fullname: str, path=None, target=None):
        """Try to find a spec for 'fullname' on sys.path or 'path'.
        The search is based on sys.path_hooks and sys.path_importer_cache.
        """
        if not fullname.startswith(__name__ + "."):
            return None
        fullname = fullname.replace(__name__, MAIN_PACKAGE, 1)

        # implement a custom loader for __main__
        if fullname.endswith("__main__"):
            return importlib.util.spec_from_loader(fullname, MainLoader())
        if fullname in sys.modules:
            return importlib.util.find_spec(fullname)
        return importlib.machinery.PathFinder.find_spec(fullname, path=path)


def add_import_hook():

    sys.meta_path.append(DiscordFinder)
    sys.modules[__name__] = sys.modules.get(MAIN_PACKAGE) or importlib.import_module(MAIN_PACKAGE)


add_import_hook()
