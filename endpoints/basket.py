from typing import List
from fastapi import APIRouter

from db.basket import Basket

router = APIRouter ()

# Basket created with creation user
#
# @router.post("/create_basket", response_model=Basket)
# async def create_basket(basket: Basket):
#     return await basket.save()


@router.get("/get_all", response_model=List[Basket])
async def get_all():
    return await Basket.objects.all()