from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def user():
    return{"Chutiya tu fir suru ho gya kya"}