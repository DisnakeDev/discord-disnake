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

from disnake.ext.commands.core import (
    MISSING,
    ApplicationCommandInteraction,
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
    BucketType,
    ChannelNotFound,
    ChannelNotReadable,
    CheckAnyFailure,
    CheckFailure,
    Cog,
    CogT,
    Command,
    CommandError,
    CommandInvokeError,
    CommandNotFound,
    CommandOnCooldown,
    CommandRegistrationError,
    CommandT,
    Context,
    ContextT,
    ConversionError,
    Cooldown,
    CooldownMapping,
    DisabledCommand,
    DynamicCooldownMapping,
    EmojiNotFound,
    ErrorT,
    ExpectedClosingQuoteError,
    ExtensionAlreadyLoaded,
    ExtensionError,
    ExtensionFailed,
    ExtensionNotFound,
    ExtensionNotLoaded,
    FlagError,
    Greedy,
    Group,
    GroupMixin,
    GroupT,
    GuildNotFound,
    GuildStickerNotFound,
    HookT,
    InvalidEndOfQuotedStringError,
    MaxConcurrency,
    MaxConcurrencyReached,
    MemberNotFound,
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
    ObjectNotFound,
    P,
    PartialEmojiConversionFailure,
    PrivateMessageOnly,
    RoleNotFound,
    T,
    ThreadNotFound,
    TooManyArguments,
    TooManyFlags,
    UnexpectedQuoteError,
    UserInputError,
    UserNotFound,
    __dict__ as __original_dict__,
    _BaseCommand,
    _CaseInsensitiveDict,
    after_invoke,
    before_invoke,
    bot_has_any_role,
    bot_has_guild_permissions,
    bot_has_permissions,
    bot_has_role,
    check,
    check_any,
    command,
    cooldown,
    dm_only,
    dynamic_cooldown,
    get_converter,
    get_signature_parameters,
    group,
    guild_only,
    has_any_role,
    has_guild_permissions,
    has_permissions,
    has_role,
    hooked_wrapped_callback,
    is_nsfw,
    is_owner,
    max_concurrency,
    run_converters,
    unwrap_function,
    wrap_callback,
)

__all__ = (
    "Command",
    "Group",
    "GroupMixin",
    "command",
    "group",
    "has_role",
    "has_permissions",
    "has_any_role",
    "check",
    "check_any",
    "before_invoke",
    "after_invoke",
    "bot_has_role",
    "bot_has_permissions",
    "bot_has_any_role",
    "cooldown",
    "dynamic_cooldown",
    "max_concurrency",
    "dm_only",
    "guild_only",
    "is_owner",
    "is_nsfw",
    "has_guild_permissions",
    "bot_has_guild_permissions",
)

locals().update(__original_dict__)

del __original_dict__
