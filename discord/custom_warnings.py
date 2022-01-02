from disnake.custom_warnings import ConfigWarning, DiscordWarning, SyncWarning

__all__ = ("DiscordWarning", "ConfigWarning", "SyncWarning")

from disnake.custom_warnings import __dict__ as __original_dict__
locals().update(__original_dict__)
