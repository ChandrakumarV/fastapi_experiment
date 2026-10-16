from typing import Annotated
from fastapi import APIRouter, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal

router = APIRouter(prefix="/validation", tags=["Query Param Validation"])


# validation with default so it's become options query
@router.get("/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=50,
            # pattern="^fixedquery$",
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# required with condition validate
@router.get("/required")
async def read_items(
    q: Annotated[
        str | None,
        Query(min_length=3, alias="test-q"),
    ],
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# You can use Pydantic models to declare query parameters in FastAPI. 😎
# Query Parameters with a Pydantic Model
class FilterParams(BaseModel):
    model_config = {
        "extra": "forbid"
    }  # if user send extra query param it's won't allow

    limit: int = Field(100, gt=2, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@router.get("/multiple-param")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
