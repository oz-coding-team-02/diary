from app.core.config import settings

TORTOISE_CONFIG = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "app.models.diary",
                "app.models.quote",
                "app.models.question",
                "app.models.bookmark",
                "aerich.models",
            ],
            "default_connection": "default",
        },
    },
}
