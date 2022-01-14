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
    from disnake.state import (
        MISSING,
        AllowedMentions,
        ApplicationCommandInteraction,
        ApplicationCommandType,
        ApplicationFlags,
        AutoShardedConnectionState,
        BaseActivity,
        CategoryChannel,
        ChannelType,
        ChunkRequest,
        ClientUser,
        ComponentType,
        ConnectionState,
        DMChannel,
        Emoji,
        GroupChannel,
        Guild,
        GuildApplicationCommandPermissions,
        GuildScheduledEvent,
        GuildSticker,
        Intents,
        Interaction,
        Invite,
        Member,
        MemberCacheFlags,
        Message,
        MessageInteraction,
        NewsChannel,
        Object,
        PartialEmoji,
        PartialGuildApplicationCommandPermissions,
        PartialMessageable,
        RawBulkMessageDeleteEvent,
        RawGuildScheduledEventUserActionEvent,
        RawIntegrationDeleteEvent,
        RawMessageDeleteEvent,
        RawMessageUpdateEvent,
        RawReactionActionEvent,
        RawReactionClearEmojiEvent,
        RawReactionClearEvent,
        RawTypingEvent,
        Role,
        StageChannel,
        StageInstance,
        Status,
        StoreChannel,
        TextChannel,
        Thread,
        ThreadMember,
        User,
        View,
        ViewStore,
        VoiceChannel,
        _channel_factory,
        _integration_factory,
        application_command_factory,
        logging_coroutine,
        try_enum,
        utils,
    )

# isort: split
from disnake.state import __dict__ as __original_dict__

locals().update(__original_dict__)
