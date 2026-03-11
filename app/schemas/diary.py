from pydantic import BaseModel,Field
from typing import List

class DiaryBase(BaseModel):
    title: str
    content: str

class DiaryBaseResponse(DiaryBase):
    id:int | None = None

class DiaryCreateRequest(DiaryBase):
    pass

class DiaryCreateResponse(DiaryBase):
    pass

#user가 작성한 diaries 조회 response 스키마
class DiaryGetResponse(BaseModel):
    diaries: List[DiaryBaseResponse]
    user:str = Field(...,max_length=255)
    total_count :int = Field(...,ge=0)

class DiaryGetRequest(DiaryBase):
    pass
