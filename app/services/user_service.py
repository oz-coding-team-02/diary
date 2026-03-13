from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from app.repositories.user_repo import UserRepo
from app.core.security import hash_token
from app.core.security import verify_password, create_access_token, decode_access_token
from app.schemas.user import UserBase, TokenResponse
from app.models.user import User
from app.models.blacklisted_token import BlacklistedToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    async def signup_user(self, data: UserBase):
        if await self.repo.check_exists(data.useremail):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="이미 등록된 이메일입니다.",
            )

        return await self.repo.create_user(
            useremail=data.useremail,
            password=data.password,
        )

    async def login_user(self, data: UserBase) -> TokenResponse:
        user = await self.repo.get_by_useremail(data.useremail)
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


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    repo: UserRepo = Depends(get_user_repo),  # 앞서 만든 DI 함수 활용
) -> User:
    token_hash = hash_token(token)
    is_blacklisted = await BlacklistedToken.filter(token_hash=token_hash).exists()

    if is_blacklisted:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="로그아웃 상태입니다. 다시 로그인해주세요.",
        )

    useremail = decode_access_token(token)
    user = await repo.get_by_useremail(useremail)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 사용자입니다.",
        )

    return user
