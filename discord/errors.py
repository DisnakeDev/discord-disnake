from disnake.errors import (
    ClientException,
    ConnectionClosed,
    DiscordException,
    DiscordServerError,
    Forbidden,
    GatewayNotFound,
    HTTPException,
    InteractionException,
    InteractionNotResponded,
    InteractionResponded,
    InteractionTimedOut,
    InvalidArgument,
    InvalidData,
    LoginFailure,
    NoMoreItems,
    NotFound,
    PrivilegedIntentsRequired,
    _flatten_error_dict,
)

__all__ = (
    "DiscordException",
    "ClientException",
    "NoMoreItems",
    "GatewayNotFound",
    "HTTPException",
    "Forbidden",
    "NotFound",
    "DiscordServerError",
    "InvalidData",
    "InvalidArgument",
    "LoginFailure",
    "ConnectionClosed",
    "PrivilegedIntentsRequired",
    "InteractionException",
    "InteractionTimedOut",
    "InteractionResponded",
    "InteractionNotResponded",
)

from disnake.errors import __dict__ as __original_dict__
locals().update(__original_dict__)
