from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

todos = []
print(todos)
# create api

class TodoModel(BaseModel):
    id: int
    title:str
    note:str
    completed:bool

@app.post("/todo")
def createTodo(todo:TodoModel):
    todos.append(todo)
    return {
        "message":"Todo is created",
        "data":todo
    }

# get todos

@app.get("/todo")
def get_todo():
    return todos

# pata parameter to search todo by id

@app.get("/todo/{todo_id}")
def todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    return {"message": "id not match plz check id again"}

# update todo using id

@app.put("/todo/{id}")
def updateTOdo(id:int, updateTodo:TodoModel):
    for index, todo in enumerate(todos):
        if todo.id==id:
            todos[index]=updateTodo
            return{
                "message":"Data Update",
                "data":updateTodo
            }
    return {"error": "Todo not found"}


# delete todo using id

@app.delete("/todo/{id}")
def deleteTodo(id:int):
    for index, todo in enumerate(todos):
        if todo.id==id:
            todos.pop(index)
            return {"message":"Message Deleted"}
    return {"error": "Todo not found"}
   
