from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List
from app.schemas.quote import BookmarkedQuoteRead

class UserBase(BaseModel):
    useremail: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    useremail: EmailStr

    # dict, orm 전환
    model_config = ConfigDict(from_attributes=True)

class UserMeRead(UserRead):
    bookmarks: List[BookmarkedQuoteRead] = []


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"