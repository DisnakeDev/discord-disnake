from disnake.custom_warnings import (
    ConfigWarning,
    DiscordWarning,
    SyncWarning,
    __dict__ as __original_dict__,
)

__all__ = ("DiscordWarning", "ConfigWarning", "SyncWarning")

locals().update(__original_dict__)

del __original_dict__
