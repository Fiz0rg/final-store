from hashlib import new
from pprint import pprint
from fastapi import HTTPException

from db.category import Category
from db.product import Product

from schemas.product import ProductCreate

class ProductRepository:

    async def create_product(user_input: ProductCreate):
        find_category = await Category.objects.get(id=user_input.category_id)
        if not find_category:
            raise HTTPException(status_code=404, detail="Category not found")
        new_product = await Product(name=user_input.name, category=find_category).save()

        return new_product

    async def get_product_by_name(product_name: str):
        return await Product.objects.select_related("category").get(name=product_name)