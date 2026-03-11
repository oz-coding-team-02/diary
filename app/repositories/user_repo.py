from app.models.user import User

class UserRepo:
    @staticmethod
    async def get_by_useremail(useremail: str) -> User:
        return await User.get_or_none(useremail=useremail)

    @staticmethod
    async def check_exists(useremail: str) -> bool:
        return await User.filter(useremail=useremail).exists()

    @staticmethod
    async def create_user(useremail: str, password_hash: str) -> User:
        return await User.create(
            useremail=useremail,
            password_hash=password_hash
        )