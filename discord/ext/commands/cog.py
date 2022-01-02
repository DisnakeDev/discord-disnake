from disnake.ext.commands.cog import (
    Cog,
    CogMeta,
    CogT,
    FuncT,
    InvokableApplicationCommand,
    InvokableMessageCommand,
    InvokableSlashCommand,
    InvokableUserCommand,
    MISSING,
    _BaseCommand,
    _cog_special_method,
)

__all__ = ("CogMeta", "Cog")

from disnake.ext.commands.cog import __dict__ as __original_dict__
locals().update(__original_dict__)
