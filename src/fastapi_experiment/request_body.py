# Request body detected by

# Path parameter  : The parameter name appears in the URL path, such as {user_id}.
# Query parameter : A simple type such as str, int, or bool that isn't declared in the path.
# Request body    : Usually a Pydantic model, such as User.

from pydantic import BaseModel
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


# typed value in body -------
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/items/typed-body")
async def create_item(item: Item):
    return item


# typed value in body
@router.post("/items/embed")
async def create_item(item: Annotated[Item, Body(embed=True)]):
    return item


# {
#   "item": {
#         ...
#   }
# }
