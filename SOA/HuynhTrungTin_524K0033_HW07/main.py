from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx


# uvicorn main:course_app --reload --port 8000
course_app = FastAPI(title="Course Service")


class Course(BaseModel):
    course_id: int
    course_name: str
    available_slots: int


courses = [
    {
        "course_id": 1,
        "course_name": "Service-Oriented Architecture",
        "available_slots": 30
    },
    {
        "course_id": 2,
        "course_name": "Web Application Development",
        "available_slots": 25
    },
    {
        "course_id": 3,
        "course_name": "Artificial Intelligence",
        "available_slots": 0
    }
]


@course_app.get("/courses", response_model=list[Course])
def get_courses():
    return courses


@course_app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int):
    for course in courses:
        if course["course_id"] == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# uvicorn main:enrollment_app --reload --port 8001
enrollment_app = FastAPI(title="Enrollment Service")

COURSE_SERVICE_URL = "http://127.0.0.1:8000"


class EnrollmentCreate(BaseModel):
    student_id: str
    student_name: str
    course_id: int


class Enrollment(BaseModel):
    enrollment_id: int
    student_id: str
    student_name: str
    course_id: int
    course_name: str


enrollments = []


@enrollment_app.get("/enrollments", response_model=list[Enrollment])
def get_enrollments():
    return enrollments


@enrollment_app.get("/enrollments/{enrollment_id}", response_model=Enrollment)
def get_enrollment(enrollment_id: int):
    for enrollment in enrollments:
        if enrollment["enrollment_id"] == enrollment_id:
            return enrollment

    raise HTTPException(
        status_code=404,
        detail="Enrollment not found"
    )


@enrollment_app.post("/enrollments", response_model=Enrollment)
def create_enrollment(enrollment: EnrollmentCreate):
    course_url = (
        f"{COURSE_SERVICE_URL}/courses/{enrollment.course_id}"
    )

    try:
        response = httpx.get(
            course_url,
            timeout=3.0
        )
    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Course Service is unavailable"
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Invalid course: Course does not exist"
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail="Error communicating with Course Service"
        )

    course = response.json()

    if course["available_slots"] <= 0:
        raise HTTPException(
            status_code=409,
            detail="Course has no available slots"
        )

    new_enrollment = {
        "enrollment_id": len(enrollments) + 1,
        "student_id": enrollment.student_id,
        "student_name": enrollment.student_name,
        "course_id": course["course_id"],
        "course_name": course["course_name"]
    }

    enrollments.append(new_enrollment)
    return new_enrollment