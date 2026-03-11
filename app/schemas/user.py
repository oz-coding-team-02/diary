from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    useremail: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    useremail: EmailStr

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"