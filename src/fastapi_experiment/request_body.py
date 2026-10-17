# Request body detected by

# Path parameter  : The parameter name appears in the URL path, such as {user_id}.
# Query parameter : A simple type such as str, int, or bool that isn't declared in the path.
# Request body    : Usually a Pydantic model, such as User.

from pydantic import BaseModel, HttpUrl
from fastapi import APIRouter, Body
from typing import Annotated

router = APIRouter(
    prefix="/requests",
    tags=["Request Body"],
)


# Singular values in body ----------
@router.post("/items/primitive")
async def create_item(quantity: str = Body()):
    return {"quantity": quantity}


# Pure list (array of object) ---------
class Image(BaseModel):
    url: HttpUrl
    name: str


@router.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images


# Typed value in body (obj) -------------
class Item(BaseModel):
    # if user send extra query param it's won't allow. API will fail
    model_config = {"extra": "forbid"}

    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/items/typed-body")
async def create_item(item: Item):
    return item


# Embbeded -------
# {
#   "item": {
#         ...
#   }
# }
@router.post("/items/embed")
async def create_item(item: Annotated[Item, Body(embed=True)]):
    return item


# Deeply nested modal body (obj of obj)
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@router.post("/offers/")
async def create_offer(offer: Offer):
    return offer
