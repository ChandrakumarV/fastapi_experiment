# When you declare other function parameters that are not part
# of the path parameters, they are automatically interpreted as "query" parameters.
from fastapi import APIRouter

router = APIRouter(
    prefix="/querys",
    tags=["Query Params"],
)

fake_items_db = [{"user_name": "Foo"}, {"user_name": "Bar"}, {"user_name": "Baz"}]


@router.get("/users")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# Optional parameters
@router.get("/users/{user_id}")
async def read_item(user_id: str, q: str | None = None):
    if q:
        return {"user_id": user_id, "q": q}
    return {"user_id": user_id}


# Query parameter type conversion
# Bool (1,0,true,false,True,False,no,yes)
@router.get("/users/type/{user_id}")
async def read_item(user_id: str, short: bool = False):
    item = {"user_id": user_id, "short": short, "type": str(type(short))}

    return item
