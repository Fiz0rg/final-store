from typing import List

from fastapi import APIRouter, Security

from repository.product import ProductRepository

from db.user import Buyer
from db.product import Product
from db.basket import Basket

from security.user import get_current_user
from schemas.product import ProductCreate

router = APIRouter()


@router.post("/create_product", response_model=Product)
async def create_product(product: ProductCreate):
    return await ProductRepository.create_product(product)


@router.get("/get_all_products", response_model=List[Product])
async def get_all():
    return await Product.objects.all()


@router.post("/add_product_in_basket", response_model=Basket)
async def add_product_in_basket(product_name: str, current_user: Buyer = Security(get_current_user, scopes=["buyer"])):
    return await ProductRepository.add_product_in_basket(product_name=product_name, user_id=current_user.id)