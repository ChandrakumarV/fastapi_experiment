from fastapi import FastAPI, Request
from config import settings
import time

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
def test():  # path operation function
    return {"message": "Hello World", "config": settings}


@app.get("/config")
def test():  # path operation function
    return settings


# Import and use routes
from fastapi_experiment.path_param import router as path_param_router
from fastapi_experiment.query_param import router as query_param_router
from fastapi_experiment.request_body import router as request_body_router
from fastapi_experiment.query_param_validation import (
    router as query_param_validation_router,
)
from fastapi_experiment.request_body_examples import (
    router as request_body_examples_router,
)

from fastapi_experiment.test import router as test_router

app.include_router(path_param_router)
app.include_router(query_param_router)
app.include_router(request_body_router)
app.include_router(query_param_validation_router)
app.include_router(request_body_examples_router)

app.include_router(test_router)
