from pydantic import BaseModel


class Student(BaseModel):
    first_name: str
    last_name: str
    direction: int
    num_of_course: int
    record_book: int
