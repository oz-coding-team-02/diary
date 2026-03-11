from fastapi import HTTPException, status
from app.repositories.user_repo import UserRepo
from app.core.security import verify_password, create_access_token
from app.schemas.user import UserLogin, TokenResponse


class UserService:
    @staticmethod
    async def signup_user(data: UserLogin):
        if await UserRepo.check_exists(data.useremail):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="이미 등록된 이메일입니다."
            )

        return await UserRepo.create_user(
            useremail=data.useremail,
            password=data.password,
        )

    @staticmethod
    async def login_user(data: UserLogin) -> dict:
        user = await UserRepo.get_by_useremail(data.useremail)

        if not user or not verify_password(data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="이메일 또는 비밀번호가 일치하지 않습니다."
            )

        access_token = create_access_token(subject=user.id)
        return {"access_token": access_token}