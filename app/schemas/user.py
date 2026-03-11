from pydantic import BaseModel

# 로그인, 회원가입 요청받는 데이터규격
class AuthRequest(BaseModel):
    username: str
    password: str

# 로그인 성공시 리턴하는 데이터 규격
class TokenResponse(BaseModel):
    access_token: str
    token_type: str