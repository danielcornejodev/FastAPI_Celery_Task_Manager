# FastAPI_Celery_Task_Manager
FastAPI &amp; Celery Task Manager


**FastAPI & Celery Task Manager**
This application demonstrates an asynchronous task management system using FastAPI and Celery with Redis as a message broker and task backend. The application provides a FastAPI-based RESTful API to accept task requests and execute long-running tasks in the background via Celery, allowing non-blocking, efficient handling of requests.

**Features**
FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
Celery: A distributed task queue to handle background jobs and asynchronous processing.
Redis: Used as the message broker and result backend for reliable and fast communication between FastAPI and Celery workers.

**How It Works**
Create Task: Users can submit tasks through a FastAPI POST request to /tasks/. This request will initiate a Celery task and immediately return a task ID for tracking.
Process Task: The submitted data is processed by a Celery worker running in the background. Here, processing is simulated by a delay to represent a long-running task.
Track Task Status: Users can check the status of a task using its task ID by sending a GET request to /tasks/{task_id}. The status returned can be either PENDING, SUCCESS, or FAILURE.
API Endpoints
1. Create a Task
Endpoint: POST /tasks/
Description: Triggers a background task to process data asynchronously.
Payload:
json
Copy code
{
  "task_name": "string",
  "data": "string"
}
Response:
json
Copy code
{
  "task_id": "string"
}
2. Get Task Status
Endpoint: GET /tasks/{task_id}
Description: Checks the status of a specific task using its task ID.
Response:
json
Copy code
{
  "status": "string",
  "result": "optional string (only if task completed)"
}

**Prerequisites**
Python 3.8+
Redis: Install and run Redis on your local machine (localhost:6379) or configure a different broker URL.
Celery and FastAPI dependencies, which can be installed via requirements.txt.
Setup and Installation
Clone the repository:
bash
Copy code
git clone <repository_url>
cd <repository_directory>

**Install the dependencies:**
bash
Copy code
pip install -r requirements.txt

**Start Redis on your machine:**
bash
Copy code
redis-server

Run the Celery worker:
bash
Copy code
celery -A tasks worker --loglevel=info

Start the FastAPI application:
bash
Copy code
uvicorn main:app --reload

**Example Usage**
Send a POST request to /tasks/ to create a new task. You’ll receive a unique task_id in the response.
Use this task_id in a GET request to /tasks/{task_id} to check the status of your task.
