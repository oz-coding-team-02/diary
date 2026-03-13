from pydantic import BaseModel
from datetime import datetime


class DiaryBase(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True  # Pydantic v2 (v1은 orm_mode = True)


class DiaryPlusID(DiaryBase):
    id: int
    created_at: datetime


class DiaryDelete(BaseModel):
    msg: str
    target_title: str

    class Config:
        from_attributes = True
