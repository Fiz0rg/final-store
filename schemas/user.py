from pydantic import BaseModel

class UserName(BaseModel):
    name: str


class PasswordUser(BaseModel):
    password: str


class UserCreate(UserName, PasswordUser):
    pass