from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import settings
from app.repositories.user_repo import UserRepo
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="유효하지 않은 접근입니다.",
        headers={"WWW-Authenticate": "Bearer"}
        # Bearer 방식의 토큰을 요구한다고 명시
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        useremail: str = payload.get("sub")
        # DB에서는 int여야 하지만 jwt 토큰은 str로 정의되어있음.
        # 조회 등 DB와 통신할 때는 int로 형변환

        if useremail is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = await UserRepo.get_by_useremail(useremail)

    if user is None:
        raise credentials_exception

    return user