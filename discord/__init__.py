import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import os
import sys

MAIN_PACKAGE = "disnake"


class MainLoader(importlib.abc.ExecutionLoader):
    def get_filename(self, fullname):
        spec = importlib.util.find_spec(fullname.split(".")[0])
        if not spec or not spec.origin:
            raise ImportError

        return os.path.dirname(spec.origin) + os.sep + "__main__.py"

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
        if not fullname.startswith(__name__):
            return None
        fullname = fullname.replace(__name__, MAIN_PACKAGE, 1)

        # implement a custom loader for __main__
        if fullname.endswith("__main__"):
            return importlib.util.spec_from_loader(fullname, MainLoader())
        return importlib.util.find_spec(fullname)


def add_import_hook():

    sys.meta_path.insert(0, DiscordFinder)
    sys.modules[__name__] = sys.modules.get(MAIN_PACKAGE) or importlib.import_module(MAIN_PACKAGE)


add_import_hook()
