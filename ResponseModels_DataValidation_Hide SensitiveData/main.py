from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []

class CreateModel(BaseModel):
    name: str
    email: str
    mobileNum: int
    password: str

class UserResponse(BaseModel):
    name: str
    email: str
    mobileNum: int

class MessageResponse(BaseModel):
    message: str
    data: UserResponse

@app.get("/response")
def get_response():
    return {
        "message": "This is the response",
        "data": users
    }

@app.post("/response", response_model=MessageResponse)
def create_response(user: CreateModel):
    public_user = UserResponse(
        name=user.name,
        email=user.email,
        mobileNum=user.mobileNum
    )
    users.append(public_user)

    return {
        "message": "User created",
        "data": public_user
    }