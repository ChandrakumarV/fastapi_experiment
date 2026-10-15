from fastapi import APIRouter
from collections.abc import AsyncIterable, Iterable
from fastapi.responses import StreamingResponse
import asyncio

router = APIRouter(
    prefix="/test",
    tags=["Test"],
)


message = """
Rick: (stumbles in drunkenly, and turns on the lights) Morty! You gotta come on. You got--... you gotta come with me.
Morty: (rubs his eyes) What, Rick? What's going on?
Rick: I got a surprise for you, Morty.
Morty: It's the middle of the night. What are you talking about?
Rick: (spills alcohol on Morty's bed) Come on, I got a surprise for you. (drags Morty by the ankle) Come on, hurry up. (pulls Morty out of his bed and into the hall)
Morty: Ow! Ow! You're tugging me too hard!
Rick: We gotta go, gotta get outta here, come on. Got a surprise for you Morty.
"""


@router.get("/story/stream", response_class=StreamingResponse)
async def stream_story() -> AsyncIterable[str]:
    for line in message.splitlines():
        yield line + "\n"
        await asyncio.sleep(1)  # 1-second delay between lines


@router.get("/story/streamtypeing", response_class=StreamingResponse)
async def stream_story() -> AsyncIterable[str]:
    for char in message:
        yield char
        await asyncio.sleep(0.01)  # 30ms per character
