from pydantic import BaseModel


class QuoteRead(BaseModel):
    content: str
    author: str
    is_bookmarked: bool
    
class BookmarkCreate(BaseModel):
    user_id: int
    quote_id: int

class BookmarkToggleResponse(BaseModel):
    is_bookmarked: bool
    message: str
    
class BookmarkedQuoteRead(BaseModel):
    id: int
    content: str
    author: str