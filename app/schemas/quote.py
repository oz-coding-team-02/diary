from pydantic import BaseModel


class QuoteRead(BaseModel):
    content: str
    author: str