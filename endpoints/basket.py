from typing import List
from fastapi import APIRouter

from db.basket import Basket

router = APIRouter ()


@router.get("/get_all", response_model=List[Basket])
async def get_all():
    return await Basket.objects.select_related("products").all()