from disnake.voice_client import (
    AudioPlayer,
    AudioSource,
    ClientException,
    ConnectionClosed,
    DiscordVoiceWebSocket,
    DiscordWebSocket,
    ExponentialBackoff,
    KeepAliveHandler,
    MISSING,
    ReconnectWebSocket,
    VoiceClient,
    VoiceKeepAliveHandler,
    VoiceProtocol,
    has_nacl,
    opus,
    utils,
)

__all__ = ("VoiceProtocol", "VoiceClient")

from disnake.voice_client import __dict__ as __original_dict__
locals().update(__original_dict__)
