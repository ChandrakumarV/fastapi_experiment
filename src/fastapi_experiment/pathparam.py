from enum import Enum
from fastapi import APIRouter, HTTPException, Path

router = APIRouter(
    prefix="/params",
    tags=["Path Parameters"],
)


@router.get("/users/me")
def my_detail():
    return {"message": f"Hi, Hello Chandru"}


# 1. Simple path parameter with type validation
@router.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "message": f"Fetching item {item_id}"}


# ---- Enum (Typed pathparam) ----
class ModelName(str, Enum):
    Alexnet = "alexnet"
    Resnet = "resnet"
    Lenet = "lenet"


@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.Alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# ---- Catch all routes -----
# like: [...file_path]
# defined  proper response type

from pydantic import BaseModel


class FilePathResponse(BaseModel):
    file_path: list[str]


@router.get("/files/{file_path:path}", response_model=FilePathResponse)
async def read_file(file_path: str) -> FilePathResponse:
    return {"file_path": file_path.split("/")}
