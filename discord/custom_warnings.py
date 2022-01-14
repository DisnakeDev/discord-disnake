from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from disnake.custom_warnings import ConfigWarning, DiscordWarning, SyncWarning

__all__ = (
    "DiscordWarning",
    "ConfigWarning",
    "SyncWarning",
)

# isort: split
from disnake.custom_warnings import __dict__ as __original_dict__

locals().update(__original_dict__)
