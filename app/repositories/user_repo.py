from pydantic import EmailStr
from typing import Union
from app.models.user import User
from app.core.security import get_password_hash


# noinspection PyMethodMayBeStatic
class UserRepo:
    def __init__(self):
        pass

    async def create_user(self, useremail: Union[str, EmailStr], password: str) -> User:
        hashed_password = get_password_hash(password)
        return await User.create(useremail=useremail, password_hash=hashed_password)

    async def get_by_useremail(self, useremail: Union[str, EmailStr]) -> User:
        return await User.get_or_none(useremail=useremail)

    async def check_exists(self, useremail: Union[str, EmailStr]) -> bool:
        return await User.filter(useremail=useremail).exists()
