from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from disnake.ext.commands.interaction_bot_base import (
        CFT,
        CXT,
        MISSING,
        ApplicationCommand,
        ApplicationCommandType,
        Cog,
        CommandRegistrationError,
        CommonBotBase,
        ConfigWarning,
        Context,
        InteractionBotBase,
        InvokableApplicationCommand,
        InvokableMessageCommand,
        InvokableSlashCommand,
        InvokableUserCommand,
        Option,
        PartialGuildApplicationCommandPermissions,
        SubCommand,
        SubCommandGroup,
        SyncWarning,
        T,
        _app_commands_diff,
        _show_diff,
        errors,
        message_command,
        slash_command,
        user_command,
    )

__all__ = ("InteractionBotBase",)

# isort: split
from disnake.ext.commands.interaction_bot_base import __dict__ as __original_dict__

locals().update(__original_dict__)
