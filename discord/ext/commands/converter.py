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

from disnake.ext.commands.converter import (
    _ID_REGEX,
    CONVERTER_MAPPING,
    CT,
    TT,
    ArgumentParsingError,
    BadArgument,
    BadBoolArgument,
    BadColorArgument,
    BadColourArgument,
    BadFlagArgument,
    BadInviteArgument,
    BadLiteralArgument,
    BadUnionArgument,
    BotMissingAnyRole,
    BotMissingPermissions,
    BotMissingRole,
    CategoryChannelConverter,
    ChannelNotFound,
    ChannelNotReadable,
    CheckAnyFailure,
    CheckFailure,
    ColorConverter,
    ColourConverter,
    CommandError,
    CommandInvokeError,
    CommandNotFound,
    CommandOnCooldown,
    CommandRegistrationError,
    ConversionError,
    Converter,
    DisabledCommand,
    EmojiConverter,
    EmojiNotFound,
    ExpectedClosingQuoteError,
    ExtensionAlreadyLoaded,
    ExtensionError,
    ExtensionFailed,
    ExtensionNotFound,
    ExtensionNotLoaded,
    FlagError,
    GameConverter,
    Greedy,
    GuildChannelConverter,
    GuildConverter,
    GuildNotFound,
    GuildStickerConverter,
    GuildStickerNotFound,
    IDConverter,
    InvalidEndOfQuotedStringError,
    InviteConverter,
    MaxConcurrencyReached,
    MemberConverter,
    MemberNotFound,
    MessageConverter,
    MessageNotFound,
    MissingAnyRole,
    MissingFlagArgument,
    MissingPermissions,
    MissingRequiredArgument,
    MissingRequiredFlag,
    MissingRole,
    NoEntryPointError,
    NoPrivateMessage,
    NotOwner,
    NSFWChannelRequired,
    ObjectConverter,
    ObjectNotFound,
    PartialEmojiConversionFailure,
    PartialEmojiConverter,
    PartialMessageConverter,
    PermissionsConverter,
    PrivateMessageOnly,
    RoleConverter,
    RoleNotFound,
    StageChannelConverter,
    StoreChannelConverter,
    T,
    T_co,
    TextChannelConverter,
    ThreadConverter,
    ThreadNotFound,
    TooManyArguments,
    TooManyFlags,
    UnexpectedQuoteError,
    UserConverter,
    UserInputError,
    UserNotFound,
    VoiceChannelConverter,
    __dict__ as __original_dict__,
    _actual_conversion,
    _convert_to_bool,
    _get_from_guilds,
    _utils_get,
    clean_content,
    get_converter,
    is_generic_type,
    run_converters,
)

__all__ = (
    "Converter",
    "ObjectConverter",
    "MemberConverter",
    "UserConverter",
    "MessageConverter",
    "PartialMessageConverter",
    "TextChannelConverter",
    "InviteConverter",
    "GuildConverter",
    "RoleConverter",
    "GameConverter",
    "ColourConverter",
    "ColorConverter",
    "VoiceChannelConverter",
    "StageChannelConverter",
    "EmojiConverter",
    "PartialEmojiConverter",
    "CategoryChannelConverter",
    "IDConverter",
    "StoreChannelConverter",
    "ThreadConverter",
    "GuildChannelConverter",
    "GuildStickerConverter",
    "PermissionsConverter",
    "clean_content",
    "Greedy",
    "run_converters",
)

locals().update(__original_dict__)

del __original_dict__
