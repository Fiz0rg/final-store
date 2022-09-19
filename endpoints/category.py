from typing import List

from fastapi import APIRouter

from db.category import Category

router = APIRouter()


@router.post("/create_category", response_model=Category)
async def create_category(category_name: str):
    new_category = await Category.objects.create(name=category_name)
    return new_category


@router.get("/get_all", response_model=List[Category])
async def get_all_categories():
    return await Category.objects.all()
    