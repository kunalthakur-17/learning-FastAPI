from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def user():
    return{"Chutiya tu fir suru ho gya kya"}

@app.get("/contact")
def contact():
    return {"This is contact api"}