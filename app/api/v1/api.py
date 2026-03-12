from fastapi import APIRouter
from app.api.v1.auth import router as auth_router
from app.api.v1.diary import router as diary_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(diary_router, prefix="/diary", tags=["diary"])