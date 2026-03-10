from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.db.database import TORTOISE_CONFIG
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

register_tortoise(
    app,
    config=TORTOISE_CONFIG,
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"message": "Diary API Server is running"}