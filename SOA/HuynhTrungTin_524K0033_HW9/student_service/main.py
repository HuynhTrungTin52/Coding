from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = [
    {
        "student_id": "524K0032",
        "student_name": "Nghia",
        "email": "nn@example.com",
    },
    {
        "student_id": "524V0007",
        "student_name": "Nhu",
        "email": "nnn@example.com",
    },
    {
        "student_id": "524K0033",
        "student_name": "Tin",
        "email": "n@example.com",
    },
]


class Student(BaseModel):
    student_id: str
    student_name: str
    email: str


@app.get("/students", response_model=list[Student])
async def get_students():
    return students


@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: str):
    student = next(
        (student for student in students if student["student_id"] == student_id),
        None,
    )
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
