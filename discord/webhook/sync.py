from disnake.webhook.sync import (
    DeferredLock,
    SyncWebhook,
    SyncWebhookMessage,
    WebhookAdapter,
    _WebhookContext,
    _context,
    _get_webhook_adapter,
)

__all__ = ("SyncWebhook", "SyncWebhookMessage")
