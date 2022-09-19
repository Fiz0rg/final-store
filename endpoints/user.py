from typing import List
from fastapi import APIRouter

from schemas.user import UserName, UserCreate
from db.user import User
from repository.user import UserRepository


router = APIRouter()


@router.post("/registration", response_model=UserName)
async def create_user(new_user: UserCreate):
    return await UserRepository.create(new_user, User)



@router.get("/get_all", response_model=List[User])
async def get_all():
    return await User.objects.all()
