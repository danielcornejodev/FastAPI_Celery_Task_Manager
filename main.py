from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from tasks import process_data  # Import the task from tasks.py

app = FastAPI()

# Define the data model using Pydantic
class Task(BaseModel):
    task_name: str
    data: str

@app.post("/tasks/")
async def create_task(task: Task):
    # Trigger Celery task asynchronously
    task_result = process_data.apply_async(args=[task.data])  
    return {"task_id": task_result.id}

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    task = process_data.AsyncResult(task_id)
    if task.state == "PENDING":
        return {"status": "Task is still processing"}
    elif task.state == "SUCCESS":
        return {"status": "Task completed", "result": task.result}
    else:
        return {"status": "Task failed"}
