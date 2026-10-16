from fastapi import FastAPI
from fastapi_experiment.config import settings

app = FastAPI()


@app.get("/")
def test():  # path operation function
    return {"message": "Hello World", "config": settings}


@app.get("/config")
def test():  # path operation function
    return settings


from fastapi_experiment.path_param import router as path_param_router
from fastapi_experiment.query_param import router as query_param_router
from fastapi_experiment.request_body import router as request_body_router
from fastapi_experiment.query_param_validation import (
    router as query_param_validation_router,
)

from fastapi_experiment.test import router as test_router

app.include_router(path_param_router)
app.include_router(query_param_router)
app.include_router(request_body_router)
app.include_router(query_param_validation_router)

app.include_router(test_router)
