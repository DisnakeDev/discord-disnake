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

from disnake.client import (
    MISSING,
    AllowedMentions,
    AppInfo,
    ApplicationCommand,
    ApplicationCommandType,
    ApplicationFlags,
    BaseActivity,
    ChannelType,
    Client,
    ClientException,
    ClientUser,
    ConnectionClosed,
    ConnectionState,
    Coro,
    DiscordException,
    DiscordServerError,
    DiscordVoiceWebSocket,
    DiscordWebSocket,
    Emoji,
    ExponentialBackoff,
    Forbidden,
    GatewayNotFound,
    Guild,
    GuildApplicationCommandPermissions,
    GuildIterator,
    GuildSticker,
    HTTPClient,
    HTTPException,
    Intents,
    InteractionException,
    InteractionNotResponded,
    InteractionResponded,
    InteractionTimedOut,
    InvalidArgument,
    InvalidData,
    Invite,
    KeepAliveHandler,
    LoginFailure,
    MessageCommand,
    NoMoreItems,
    NotFound,
    Object,
    PartialGuildApplicationCommandPermissions,
    PartialMessageable,
    PrivilegedIntentsRequired,
    ReconnectWebSocket,
    SlashCommand,
    StageInstance,
    StandardSticker,
    Status,
    StickerPack,
    Template,
    Thread,
    User,
    UserCommand,
    View,
    VoiceClient,
    VoiceKeepAliveHandler,
    VoiceRegion,
    Webhook,
    Widget,
    __dict__ as __original_dict__,
    _cancel_tasks,
    _cleanup_loop,
    _sticker_factory,
    _threaded_channel_factory,
    create_activity,
    utils,
)

__all__ = ("Client",)

locals().update(__original_dict__)

del __original_dict__
