from enum import Enum
from fastapi import APIRouter, HTTPException, Path

router = APIRouter(
    tags=["Path Parameters"],
)


@router.get("/users/me")
def my_detail():
    return {"message": f"Hi, Hello Chandru"}


# 1. Simple path parameter with type validation
@router.get("/users/{user_id}")
def get_item(user_id: int):
    return {
        "User id": user_id,
    }


# ---- Enum (Typed pathparam) ----
class UserName(str, Enum):
    Chandru = "chandru"
    Naresh = "naresh"
    Ram = "ram"


@router.get("/users/name/{user_name}")
async def get_by_username(user_name: UserName):
    if user_name is UserName.Chandru:
        return {"user_name": user_name, "message": "Good Boy"}

    if user_name.value == "lenet":
        return {"user_name": user_name, "message": "Average Boy"}

    return {"user_name": user_name, "message": "Bad Boy"}


# ---- Catch all routes -----
# like: [...file_path]
# defined  proper "response" type

from pydantic import BaseModel


class FilePathResponse(BaseModel):
    file_path: list[str]


@router.get("/files/{file_path:path}", response_model=FilePathResponse)
async def read_file(file_path: str) -> FilePathResponse:
    return {"file_path": file_path.split("/")}
