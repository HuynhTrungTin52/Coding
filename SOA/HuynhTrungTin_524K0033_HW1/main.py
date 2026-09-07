from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr, ValidationError

class Student(BaseModel):
    student_id : str = Field(min_length=1)
    name : str = Field(min_length=2)
    age : int = Field(ge=18,le=60)
    email: EmailStr
    gpa : float = Field(ge=0.0,le=4.0)
    
    
external_data =[
    {"student_id":"524k0001",
  "name":"A1",
  "age":18,
  "email":"A1@gmail.com",
  "gpa":0},
 {"student_id":"524k0002",
   "name":"A2",
   "age":19,
   "email":"A2@gmail.com",
   "gpa":1},
  {"student_id":"524k0003",
    "name":"A3",
    "age":14,
    "email":"A4@gmail.com",
    "gpa":0.5},
   {"student_id":"",
     "name":"A5",
     "age":20,
     "email":"A5@gmail.com",
     "gpa":4},
    {"student_id":"524k0030",
      "name":"AaA",
      "age":25,
      "email":"AaA@gmail.com",
      "gpa":3.8},
]

valid_students=[]
invalid_students=[]

for student in external_data:
    try:
        is_student=Student.model_validate(student)
        valid_students.append(is_student)
    except ValidationError as e:
      invalid_students.append(student)
      for err in e.errors():
        print(f"Field: {err['loc'][0]} -> Error: {err['msg']}")

app = FastAPI()

@app.get("/")
async def info():
    return {"service":"Student Service",
            "course":"504070"}
    
@app.get("/health")
async def status():
    return{"status":"healthy"}

@app.get("/students")
async def return_students():
    return valid_students

@app.get("/students/{student_id}")
async def return_student_id(student_id):
    is_student=next((student for student in valid_students if student.student_id==student_id),None)
    if is_student == None:
        raise HTTPException(status_code=404,detail="Student not found")
    
    return is_student

# for student in valid_students:
#     attrs = vars(student)
#     print(attrs["student_id"])