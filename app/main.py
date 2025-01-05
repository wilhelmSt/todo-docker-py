from fastapi import FastAPI
from routes.todos import router as todos_router

app = FastAPI(title="To-Do List API", version="1.0.0")

app.include_router(todos_router, prefix="/api/todos", tags=["To-Dos"])
