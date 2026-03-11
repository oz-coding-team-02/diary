from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.db.database import TORTOISE_CONFIG
from app.core.config import settings
from app.api.v1.auth import router as auth_router

from app.api.v1.diary import diary_router as diary_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

register_tortoise(
    app,
    config=TORTOISE_CONFIG,
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API"}


app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(diary_router, prefix="/api/v1/diaries", tags=["Diary"])