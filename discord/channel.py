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

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from disnake.channel import (
        DMC,
        MISSING,
        ArchivedThreadIterator,
        Asset,
        CategoryChannel,
        ChannelType,
        ClientException,
        DMChannel,
        GroupChannel,
        Hashable,
        InvalidArgument,
        NewsChannel,
        Object,
        PartialMessageable,
        PermissionOverwrite,
        Permissions,
        StageChannel,
        StageInstance,
        StagePrivacyLevel,
        StoreChannel,
        TextChannel,
        Thread,
        VideoQualityMode,
        VocalGuildChannel,
        VoiceChannel,
        VoiceRegion,
        _channel_factory,
        _channel_type_factory,
        _guild_channel_factory,
        _single_delete_strategy,
        _threaded_channel_factory,
        _threaded_guild_channel_factory,
        try_enum,
        try_enum_to_int,
        utils,
    )

__all__ = (
    "TextChannel",
    "VoiceChannel",
    "StageChannel",
    "DMChannel",
    "CategoryChannel",
    "NewsChannel",
    "StoreChannel",
    "GroupChannel",
    "PartialMessageable",
)

# isort: split
from disnake.channel import __dict__ as __original_dict__

locals().update(__original_dict__)
