from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt
from app.core.config import settings

# bcrypt 알고리즘 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# jwt 설정
ALGORITHMS = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

# 비밀번호 해싱
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# 비밀번호 일치여부 TF 검증
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# jwt 액세스 토큰 생성
def create_access_token(subject: Union[str, Any]) -> str:
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHMS)
    return encoded_jwt