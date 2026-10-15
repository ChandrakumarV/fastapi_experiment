from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def test():
    return {"message": "Hello World"}


from fastapi_experiment.pathparam import router as pathparam_router

app.include_router(pathparam_router)
