from disnake.webhook.sync import (
    BaseWebhook,
    DeferredLock,
    DiscordServerError,
    Forbidden,
    HTTPException,
    InvalidArgument,
    MISSING,
    Message,
    NotFound,
    PartialMessageable,
    Route,
    SyncWebhook,
    SyncWebhookMessage,
    WebhookAdapter,
    _WebhookContext,
    _WebhookState,
    _context,
    _get_webhook_adapter,
    handle_message_parameters,
    utils,
)

__all__ = ("SyncWebhook", "SyncWebhookMessage")

from disnake.webhook.sync import __dict__ as __original_dict__
locals().update(__original_dict__)
