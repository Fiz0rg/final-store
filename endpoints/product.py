from typing import List
from fastapi import APIRouter

from db.product import Product

from repository.product import ProductRepository

from schemas.product import ProductCreate

router = APIRouter()


@router.post("/create_product", response_model=Product)
async def create_product(product: ProductCreate):
    return await ProductRepository.create_product(product)


@router.get("/get_all_products", response_model=List[Product])
async def get_all():
    return await Product.objects.all()