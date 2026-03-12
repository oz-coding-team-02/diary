from app.models.user import User
from app.core.security import get_password_hash


class UserRepo:
    @staticmethod
    async def create_user(useremail: str, password: str) -> User:
        hashed_password = get_password_hash(password)

        return await User.create(useremail=useremail, password_hash=hashed_password)

    @staticmethod
    async def get_by_useremail(useremail: str) -> User:
        return await User.get_or_none(useremail=useremail)

    @staticmethod
    async def check_exists(useremail: str) -> bool:
        return await User.filter(useremail=useremail).exists()
