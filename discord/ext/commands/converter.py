from disnake.ext.commands.converter import (
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
    CONVERTER_MAPPING,
    CT,
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
    NSFWChannelRequired,
    NoEntryPointError,
    NoPrivateMessage,
    NotOwner,
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
    TT,
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
    _ID_REGEX,
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

from disnake.ext.commands.converter import __dict__ as __original_dict__
locals().update(__original_dict__)
