from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DiaryBase(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True


class DiaryPlusID(DiaryBase):
    id: int
    created_at: datetime


class DiaryDelete(BaseModel):
    msg: str
    target_title: str

    class Config:
        from_attributes = True


class WritingPromptResponse(BaseModel):
    quote_id: Optional[int] = None
    quote: str
    question: str
