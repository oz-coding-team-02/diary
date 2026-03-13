from pydantic import BaseModel

class QuestionRead(BaseModel):
    content: str
