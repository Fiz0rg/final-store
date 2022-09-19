from typing import Optional

from pydantic import BaseModel

from db.category import Category


class ProductCreate(BaseModel):
    name: str
    category_id: int
