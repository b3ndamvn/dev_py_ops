from pydantic import BaseModel


class RecordBook(BaseModel):
    number: int
    subject: str
    grade: int
