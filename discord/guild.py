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
    from disnake.guild import (
        MISSING,
        Asset,
        AuditLogAction,
        AuditLogIterator,
        BanEntry,
        CategoryChannel,
        ChannelType,
        ClientException,
        Colour,
        ContentFilter,
        DMChannel,
        Emoji,
        File,
        GroupChannel,
        Guild,
        GuildApplicationCommandPermissions,
        GuildScheduledEvent,
        GuildScheduledEventEntityType,
        GuildScheduledEventMetadata,
        GuildScheduledEventPrivacyLevel,
        GuildSticker,
        Hashable,
        Integration,
        InvalidArgument,
        InvalidData,
        Invite,
        Member,
        MemberIterator,
        NewsChannel,
        NotificationLevel,
        NSFWLevel,
        PartialGuildApplicationCommandPermissions,
        PartialMessageable,
        PermissionOverwrite,
        Role,
        StageChannel,
        StageInstance,
        StagePrivacyLevel,
        StoreChannel,
        SystemChannelFlags,
        TextChannel,
        Thread,
        ThreadMember,
        User,
        VerificationLevel,
        VideoQualityMode,
        VoiceChannel,
        VoiceRegion,
        VoiceState,
        Widget,
        _guild_channel_factory,
        _GuildLimit,
        _integration_factory,
        _threaded_guild_channel_factory,
        abc,
        try_enum,
        utils,
    )

__all__ = ("Guild",)

# isort: split
from disnake.guild import __dict__ as __original_dict__

locals().update(__original_dict__)
