from fastapi import APIRouter, HTTPException, status
from app.core.security import verify_password, create_access_token, get_password_hash
from app.schemas.user import UserCreate, TokenResponse, UserLogin, UserRead
from app.repositories.user_repo import UserRepo

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def signup(data: UserCreate):
    if await UserRepo.check_exists(data.useremail):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="이미 등록된 이메일입니다."
        )

    new_user = await UserRepo.create_user(
        useremail=data.useremail,
        password_hash=get_password_hash(data.password)
    )

    return new_user

@router.post('/login', response_model=TokenResponse)
async def login(data: UserLogin):
    user = await UserRepo.get_by_useremail(user.useremail)

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="이메일 또는 비밀번호가 일치하지 않습니다."
        )

    access_token = create_access_token(subject=user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }