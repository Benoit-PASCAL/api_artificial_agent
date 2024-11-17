from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Je s'appelle Root"}


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}
