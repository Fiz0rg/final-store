from itertools import product
from fastapi import HTTPException

from db.category import Category
from db.product import Product
from db.basket import Basket

from schemas.product import ProductCreate

class ProductRepository:

    async def create_product(user_input: ProductCreate):
        print('123')
        find_category = await Category.objects.get(id=user_input.category)
        if not find_category:
            raise HTTPException(status_code=404, detail="Category not found")
        
        print(user_input)
        new_product = await Product(**user_input.dict()).save()
        print(new_product)
        print(user_input)

        return new_product


    async def get_product_by_name(product_name: str):
        return await Product.objects.select_related("category").get(name=product_name)


    async def add_product_in_basket(product_name: str, user_id: int):
        product = await Product.objects.get(name=product_name)
        user_basket = await Basket.objects.get(id=user_id)
        await user_basket.products.add(product)

        return user_basket