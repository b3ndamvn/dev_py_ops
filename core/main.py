from fastapi import FastAPI

from schemas.record_book import RecordBook
from schemas.teacher import Teacher
from schemas.student import Student

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/teachers/", response_model=Teacher)
async def create_teacher(teacher: Teacher) -> Teacher:
    pass
