from fastapi import APIRouter, HTTPException, status
from app.core.security import get_password_hash, verify_password, create_access_token
from app.schemas.user import AuthRequest, TokenResponse, SignupResponse
from app.repositories.user_repo import UserRepo

router = APIRouter()


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=SignupResponse)
async def signup(data: AuthRequest):
    if await UserRepo.check_exists(data.useremail):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 이메일 입니다.")

    new_user = await UserRepo.create_user(
        useremail=data.useremail,
        password_hash=data.password_hash,
    )

    return {
        'id': new_user.id,
        'useremail': new_user.useremail,
        'message': '회원가입이 성공적으로 완료되었습니다.'
    }


@router.post('/login', response_model=TokenResponse)
async def login(data: AuthRequest):
    user = await UserRepo.get_by_useremail(data.useremail)

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="이메일 또는 비밀번호가 일치하지 않습니다.")

    access_token = create_access_token(subject=user.id)
    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }