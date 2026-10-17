from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/test",
    tags=["Test"],
)


@router.post("/")
async def root(body: set = Body()):
    return body
