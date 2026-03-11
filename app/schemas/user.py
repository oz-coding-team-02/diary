from pydantic import BaseModel, EmailStr


class UserLogin(BaseModel):
    useremail: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    useremail: EmailStr

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"