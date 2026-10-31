from fastapi import FastAPI

app = FastAPI()



# multipal routes
# home 

@app.get("/")
def home():
    return {"message": "This is my home route"}

@app.get("/about")
def about():
    return {"message": "This is my about page"}


@app.get("/user")
def user():
    return {
       "user1" : {
            "userName":"Kunal Thakur",
                   "Age": 27,
                   "work":"Software developer"
       },
       "user2":{
            "userName":"Arti",
                   "Age": 25,
                   "work":"Data entry and sales"
       }
    }
# #  Path Parameters

@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {"user_id": user_id}



 #  Query Parameters

@app.get("/users")
def get_users(name:str=None):
    return{"search name: " : name}

@app.get("/product")
def get_product(limit: int=100):
    return {"this is total limit": limit}

# # Multipal Query Parameters 

@app.get("/items")
def get_items(name:str=None, price:int=0, status:bool=True):
    return{
        "user":{
            "name": name,
            "price": price,
            "status":status,
        }
    }