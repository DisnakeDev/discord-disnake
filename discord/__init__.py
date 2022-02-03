"""
Discord API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Discord API.

:copyright: (c) 2015-present Rapptz
:license: MIT, see LICENSE for more details.

"""


def _add_import_hook():
    import importlib
    import importlib.machinery
    import importlib.util
    import sys

    class DiscordFinder(importlib.machinery.PathFinder):
        @classmethod
        def find_spec(cls, fullname: str, path=None, target=None):
            """Try to find a spec for 'fullname' on sys.path or 'path'.
            The search is based on sys.path_hooks and sys.path_importer_cache.
            """
            if not fullname.startswith("discord"):
                return None
            fullname = fullname.replace("discord", "disnake")
            return importlib.util.find_spec(fullname)

    sys.meta_path.insert(0, DiscordFinder)
    sys.modules["discord"] = sys.modules.get("disnake") or importlib.import_module("disnake")


_add_import_hook()
del _add_import_hook

from disnake import *
