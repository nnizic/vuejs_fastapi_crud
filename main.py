from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the frontend URL in production
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "HEAD"],
    allow_headers=["*"],
)

# Your CRUD routes and database code...

# Mock database
todos = []


class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None


@app.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo):
    todos.append(todo)
    return todo


@app.get("/todos/", response_model=List[Todo])
async def read_todos():
    return todos


@app.get("/todos/{todo_id}", response_model=Todo)
async def read_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: Todo):
    for idx, existing_todo in enumerate(todos):
        if existing_todo.id == todo_id:
            todos[idx] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}", response_model=Todo)
async def delete_todo(todo_id: int):
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[idx]
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")
