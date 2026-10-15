# Request body detected by

# Path parameter  : The parameter name appears in the URL path, such as {user_id}.
# Query parameter : A simple type such as str, int, or bool that isn't declared in the path.
# Request body    : Usually a Pydantic model, such as User.

from pydantic import BaseModel
from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/requests",
    tags=["Request Body"],
)


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/items/")
async def create_item(item: Item):
    return item


@router.post("/items/test")
async def create_item(quantity: str = Body()):
    return {"quantity": quantity}
