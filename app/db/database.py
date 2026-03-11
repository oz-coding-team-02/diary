from app.core.config import settings

TORTOISE_CONFIG = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "app.models.quote",
                "app.models.diary",
                "app.models.question",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}
