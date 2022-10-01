from typing import Optional, List
from ormar import ForeignKey, Model, Integer

from .product import Product
from .user import Buyer
from .base_class import MetaClass


class Basket(Model):
    class Meta(MetaClass):
        tablename = "basket"

    id: int = Integer(primary_key=True)
    user_id: Optional[Buyer] = ForeignKey(Buyer, skip_reverse=True)
    prudocts: Optional[Product] = ForeignKey(Product, skip_reverse=True)