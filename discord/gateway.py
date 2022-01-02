from disnake.gateway import (
    BaseActivity,
    ConnectionClosed,
    DiscordClientWebSocketResponse,
    DiscordVoiceWebSocket,
    DiscordWebSocket,
    EventListener,
    GatewayRatelimiter,
    InvalidArgument,
    KeepAliveHandler,
    ReconnectWebSocket,
    SpeakingState,
    VoiceKeepAliveHandler,
    WebSocketClosure,
)

__all__ = (
    "DiscordWebSocket",
    "KeepAliveHandler",
    "VoiceKeepAliveHandler",
    "DiscordVoiceWebSocket",
    "ReconnectWebSocket",
)

from disnake.gateway import __dict__ as __original_dict__
locals().update(__original_dict__)
