from app.core.config import settings

TORTOISE_CONFIG = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models.user", "aerich.models"],
            "default_connection": "default",
        },
    },
}