from fastapi import APIRouter, status, HTTPException

from app.repositories.quote_repo import QuoteRepository
from app.schemas.quote import QuoteRead

router = APIRouter(prefix="/api/v1/quote", tags=["Quote"])

@router.get("", status_code=status.HTTP_200_OK, response_model=QuoteRead)
async def get_quote():
    quote = QuoteRepository.get_random_quote_one()
    if quote is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Quote not found")
    return quote
