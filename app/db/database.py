import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

TORTOISE_CONFIG = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            # app/models/ 아래의 모든 파일들을 등록
            "models": [
                "app.models.user",
                "app.models.diary",
                "app.models.quote",
                "app.models.question",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}