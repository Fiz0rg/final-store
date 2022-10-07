from typing import List
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from cloudipsp import Api, Checkout

from db.product import Product

from db.basket import Basket

router = APIRouter()


@router.get("/get_all")
async def get_all():
    test = await Basket.objects.select_all("products").get()
    return test.products


@router.post("/purchase/{product_id}", response_class=RedirectResponse)
async def purchase(product_id: int):
    take_product = await Product.objects.get(id=product_id)

    product_price = take_product.price
    api = Api(merchant_id=1396424,
            secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": product_price
    }
    url = checkout.url(data).get('checkout_url')
    
    return url
