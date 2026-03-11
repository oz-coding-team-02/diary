from fastapi import APIRouter, HTTPException, status
from app.models.user import User
from app.core.security import get_password_hash, verify_password, create_access_token
from app.schemas.user import AuthRequest, TokenResponse

router = APIRouter()

## API 엔드포인트 -----

# 회원가입
@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(data: AuthRequest):
    user_exists = await User.filter(username=data.username).exists()
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
                            detail="이미 존재하는 계정입니다"
        )

    new_user = await User.create(
        username=data.username,
        password_hash=get_password_hash(data.password,)
    )

    return {
        'id': new_user.id,
        'username': new_user.username,

    }

@router.post('/login', response_model=TokenResponse)
async def login(data: AuthRequest):
    user = await User.get_or_none(username=data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='아이디 또는 비밀번호가 잘못되었습니다.'
        )

    if not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='아이디 또는 비밀번호가 잘못되었습니다.'
        )

    access_token = create_access_token(subject=user.id)

    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }