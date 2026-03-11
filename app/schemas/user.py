from pydantic import BaseModel, EmailStr
from fastapi.security import OAuth2PasswordBearer

from pydantic import Field


class UserCreate(BaseModel):
    useremail: EmailStr
    password: str

class UserLogin(BaseModel):
    useremail: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    useremail: EmailStr

class UserGetDiaries(BaseModel):
    id: int
    useremail: EmailStr
    page: int = Field(gt=0,lt=100)
    size: int = Field(gt=0,lt=100)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")
