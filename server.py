from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.security.oauth2 import *

from fja import endp_fja

from db.db import database
from endpoints import category, user, basket, product, product_photo

app = FastAPI(swagger_ui_init_oauth={"clientId": "0b4655d96d2bc4f1f012",
                                     "clientSecret": "45098608defa54953bb3e8b87551c0503d52bf77"})

app.state.database = database

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        print("Connecting to database")
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        print("Disconnecting from  database")
        await database_.disconnect()
        

app.include_router(category.router, tags=["category router"], prefix="/category")
app.include_router(user.router, tags=["user router"], prefix="/user")
app.include_router(basket.router, tags=["basket router"], prefix="/basket")
app.include_router(product.router, tags=["product router"], prefix="/product")
app.include_router(product_photo.router, tags=["photo"], prefix="/photo")
app.include_router(endp_fja.router, tags=["fja"], prefix="/fja")


app.mount("/static", StaticFiles(directory="static"), name="static")

