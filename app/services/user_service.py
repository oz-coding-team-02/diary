from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from app.repositories.user_repo import UserRepo
from app.core.security import verify_password, create_access_token, decode_access_token
from app.schemas.user import UserBase, TokenResponse
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    async def signup_user(self, data: UserBase):
        if await UserRepo.check_exists(data.useremail):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="이미 등록된 이메일입니다.",
            )

        return await UserRepo.create_user(
            useremail=data.useremail,
            password=data.password,
        )


    async def login_user(self, data: UserBase) -> TokenResponse:
        user = await UserRepo.get_by_useremail(data.useremail)
        if not user or not verify_password(data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="로그인 정보가 정확하지 않습니다.",
            )

        access_token = create_access_token(subject=user.useremail)
        return TokenResponse(access_token=access_token)

def get_user_repo() -> UserRepo:
    return UserRepo()

def get_user_service(repo: UserRepo = Depends(get_user_repo)) -> UserService:
    return UserService(repo=repo)


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    useremail = decode_access_token(token)

    user = await UserRepo.get_by_useremail(useremail)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 사용자입니다.",
        )

    return user

