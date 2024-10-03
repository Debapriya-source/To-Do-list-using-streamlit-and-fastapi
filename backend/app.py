from fastapi import FastAPI, HTTPException
from typing import List, Optional
from models.tasks import Task


app = FastAPI()


# Create an in-memory list to store tasks and a counter for task IDs
tasks = []
task_id_counter = 1


# Create a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    global task_id_counter
    task.id = task_id_counter
    task_id_counter += 1
    tasks.append(task)
    return task


# Get all tasks
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks


# Get a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# Update an existing task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
