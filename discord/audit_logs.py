"""
The MIT License (MIT)

Copyright (c) 2015-2021 Rapptz
Copyright (c) 2021-present Disnake Development

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from disnake.audit_logs import (
    Asset,
    AuditLogChanges,
    AuditLogDiff,
    AuditLogEntry,
    Colour,
    Hashable,
    Invite,
    Object,
    PermissionOverwrite,
    Permissions,
    T,
    _AuditLogProxyMemberDisconnect,
    _AuditLogProxyMemberMoveOrMessageDelete,
    _AuditLogProxyMemberPrune,
    _AuditLogProxyPinAction,
    _AuditLogProxyStageInstanceAction,
    _enum_transformer,
    _guild_hash_transformer,
    _transform_avatar,
    _transform_channel,
    _transform_color,
    _transform_datetime,
    _transform_guild_id,
    _transform_icon,
    _transform_member_id,
    _transform_overwrites,
    _transform_permissions,
    _transform_privacy_level,
    _transform_snowflake,
    _transform_type,
    abc,
    enums,
    utils,
)

__all__ = ("AuditLogDiff", "AuditLogChanges", "AuditLogEntry")

# isort: split
from disnake.audit_logs import __dict__ as __original_dict__

locals().update(__original_dict__)
