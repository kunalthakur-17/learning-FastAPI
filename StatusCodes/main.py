from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message:-":"Api working"}


@app.post("/create",status_code= status.HTTP_201_CREATED)
def create_user():
    return {
        "message":""
    }