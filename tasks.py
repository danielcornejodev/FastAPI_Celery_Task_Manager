from celery import Celery
import time

# Set up Celery with Redis as the broker
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def process_data(data: str):
    print(f"Processing data: {data}")
    time.sleep(5)  # Simulate a long-running task
    print(f"Completed processing: {data}")
    return f"Processed data: {data}"