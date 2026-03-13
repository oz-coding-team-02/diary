from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List
from app.schemas.quote import BookmarkedQuoteRead
from app.schemas.diary import DiaryPlusID


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
    diaries: List[DiaryPlusID] = []


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class QuoteRead(BaseModel):
    id: int
    content: str
    author: str

    class Config:
        from_attributes = True


class BookmarkRead(BaseModel):
    id: int
    quote: QuoteRead

    class Config:
        from_attributes = True