from pydantic import BaseModel, EmailStr


class AuthRequest(BaseModel):
    useremail: EmailStr
    password: str


class SignupResponse(BaseModel):
    id: int
    useremail: EmailStr
    message: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
