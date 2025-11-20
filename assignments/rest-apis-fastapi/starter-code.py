from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

# Create FastAPI application instance
app = FastAPI(title="Task Management API", description="A simple REST API for managing tasks")

# Define the Task model using Pydantic
class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=3, max_length=100, description="Task title (3-100 characters)")
    description: str = Field(..., min_length=1, description="Task description (cannot be empty)")
    completed: bool = False

# In-memory storage for tasks (in a real application, you would use a database)
tasks_db: List[Task] = []

# TODO: Implement the root endpoint
# Create a GET endpoint at "/" that returns a welcome message
@app.get("/")
async def root():
    pass  # Replace with your implementation

# TODO: Implement GET /tasks endpoint
# Return all tasks from the tasks_db list
@app.get("/tasks")
async def get_all_tasks():
    pass  # Replace with your implementation

# TODO: Implement GET /tasks/{task_id} endpoint
# Return a specific task by ID or raise HTTPException with 404 if not found
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    pass  # Replace with your implementation

# TODO: Implement POST /tasks endpoint
# Add a new task to tasks_db and return it with 201 status code
# Hint: Use response_model and status_code parameters
@app.post("/tasks", status_code=201)
async def create_task(task: Task):
    pass  # Replace with your implementation

# TODO: Implement PUT /tasks/{task_id} endpoint
# Update an existing task or raise HTTPException with 404 if not found
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    pass  # Replace with your implementation

# TODO: Implement DELETE /tasks/{task_id} endpoint
# Delete a task or raise HTTPException with 404 if not found
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    pass  # Replace with your implementation

# To run this application:
# 1. Install FastAPI and uvicorn: pip install fastapi uvicorn
# 2. Run: uvicorn starter-code:app --reload
# 3. Visit http://localhost:8000/docs to see the interactive API documentation
