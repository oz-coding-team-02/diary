from fastapi import HTTPException, status

from app.repositories.quote_repo import QuoteRepository
from app.schemas.quote import BookmarkCreate, QuoteRead, BookmarkedQuoteRead


class QuoteService:
    @staticmethod
    async def get_random_quote_or_none(user_id: int) -> QuoteRead:
        quote = await QuoteRepository.get_random_quote_one()

        if quote is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found"
            )

        is_bookmarked = (
            await QuoteRepository.get_bookmark_or_none(
                user_id=user_id, quote_id=quote.id
            )
            is not None
        )

        return QuoteRead(
            content=quote.content, author=quote.author, is_bookmarked=is_bookmarked
        )

    @staticmethod
    async def toggle_bookmark(data: BookmarkCreate) -> bool:
        bookmark = await QuoteRepository.get_bookmark_or_none(
            user_id=data.user_id, quote_id=data.quote_id
        )

        if bookmark:
            await bookmark.delete()
            return False
        else:
            await QuoteRepository.create_bookmark(
                user_id=data.user_id, quote_id=data.quote_id
            )
            return True

    @staticmethod
    async def get_bookmarked_quotes_for_user(user_id: int) -> list[BookmarkedQuoteRead]:
        bookmarks = await QuoteRepository.get_bookmarked_quotes_for_user(
            user_id=user_id
        )
        result_list = []
        for bookmark in bookmarks:
            result_list.append(
                BookmarkedQuoteRead(
                    id=bookmark.quote.id,
                    content=bookmark.quote.content,
                    author=bookmark.quote.author,
                )
            )

        return result_list
