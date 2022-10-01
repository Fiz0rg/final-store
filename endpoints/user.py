from typing import List
from fastapi import APIRouter

from schemas.user import UserName, UserCreate
from db.user import Buyer
from repository.user import UserRepository


router = APIRouter()


@router.post("/registration", response_model=UserName)
async def create_user(new_user: UserCreate):
    return await UserRepository.create(new_user, Buyer)



@router.get("/get_all", response_model=List[Buyer])
async def get_all():
    return await Buyer.objects.all()



