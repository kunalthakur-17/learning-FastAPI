from fastapi import FastAPI

app = FastAPI();

@app.get("/")
def hello():
    return {"message": "Hello word"}

@app.get("/about")
def about():
    return {"message": "This api for about you page"}