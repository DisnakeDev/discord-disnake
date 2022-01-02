from disnake.permissions import (
    BaseFlags,
    P,
    PO,
    PermissionOverwrite,
    Permissions,
    _augment_from_permissions,
    alias_flag_value,
    fill_with_flags,
    flag_value,
    make_permission_alias,
    permission_alias,
)

__all__ = ("Permissions", "PermissionOverwrite")

from disnake.permissions import __dict__ as __original_dict__
locals().update(__original_dict__)
