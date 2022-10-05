from typing import Optional, List
from ormar import ForeignKey, Model, Integer, ManyToMany

from .product import Product
from .user import Buyer
from .base_class import MetaClass


class Basket(Model):
    class Meta(MetaClass):
        tablename = "basket"

    id: int = Integer(primary_key=True)
    user_id: Optional[Buyer] = ForeignKey(Buyer, skip_reverse=True)
    products: Optional[List[Product]] = ManyToMany(Product, skip_reverse=True)