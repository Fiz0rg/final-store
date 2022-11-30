from datetime import timedelta
from typing import List

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, Security

from starlette.templating import Jinja2Templates
from starlette.requests import Request

from schemas.user import UserName, UserCreate
from schemas.token import Token

from db.user import Buyer
from repository.user import UserRepository
from security.user import create_access_token, ACCESS_TOKEN_EXPIRE_MINUNES, authenticate_user, get_current_user

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get('/')
async def google_auth(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})


@router.get("/get_all", response_model=List[Buyer])
async def get_all():
    return await Buyer.objects.all()


@router.post("/registration", response_model=UserName)
async def create_user(new_user: UserCreate):
    return await UserRepository.create(new_user, Buyer)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUNES)
    access_token = create_access_token(
        data={"sub": user.name, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}



@router.get("/users/me/", response_model=Buyer)
async def read_users_me(current_user: Buyer = Security(get_current_user, scopes=["buyer"])):
    return current_user





