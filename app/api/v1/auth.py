from fastapi import APIRouter, status, Depends, Request, HTTPException
from datetime import datetime, timezone
from app.schemas.user import TokenResponse, UserBase, UserRead
from app.services.user_service import UserService, get_user_service
from app.core.security import hash_token
from app.models.blacklisted_token import BlacklistedToken

router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def signup(data: UserBase, service: UserService = Depends(get_user_service)):
    return await service.signup_user(data)


@router.post("/login", response_model=TokenResponse)
async def login(data: UserBase, service: UserService = Depends(get_user_service)):
    return await service.login_user(data)


@router.post("/logout")
async def logout(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="존재하지 않는 토큰입니다."
        )

    token = auth_header.split()[1]

    await BlacklistedToken.get_or_create(token_hash=hash_token(token))
    return {"message": "성공적으로 로그아웃되었습니다."}
