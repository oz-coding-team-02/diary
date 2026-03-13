from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as user_router
from app.api.v1.diary import router as diary_router
from app.api.v1.quote import router as quote_router
from app.api.v1.question import router as question_router
api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(diary_router, prefix="/diary", tags=["diary"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(quote_router, prefix="/quote", tags=["quote"])
api_router.include_router(question_router, prefix="/question", tags=["question"])