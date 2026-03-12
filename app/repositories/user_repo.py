from app.models.user import User
from app.core.security import get_password_hash


class UserRepo:
    async def create_user(self, useremail: str, password: str) -> User:
        hashed_password = get_password_hash(password)

        return await User.create(useremail=useremail, password_hash=hashed_password)

    async def get_by_useremail(self, useremail: str) -> User:
        return await User.get_or_none(useremail=useremail)

    async def check_exists(self, useremail: str) -> bool:
        return await User.filter(useremail=useremail).exists()
