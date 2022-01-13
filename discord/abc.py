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

from disnake.abc import (
    GCH,
    MISSING,
    AllowedMentions,
    ChannelType,
    ClientException,
    Connectable,
    File,
    GuildChannel,
    GuildSticker,
    HistoryIterator,
    InvalidArgument,
    Invite,
    Messageable,
    PartyType,
    PermissionOverwrite,
    Permissions,
    PrivateChannel,
    Role,
    Snowflake,
    StickerItem,
    T,
    Typing,
    User,
    VoiceClient,
    VoiceProtocol,
    _Overwrites,
    _Undefined,
    _undefined,
    try_enum_to_int,
    utils,
)

__all__ = ("Snowflake", "User", "PrivateChannel", "GuildChannel", "Messageable", "Connectable")

# isort: split
from disnake.abc import __dict__ as __original_dict__

locals().update(__original_dict__)
