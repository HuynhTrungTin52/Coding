import os

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

STUDENT_SERVICE_URL = os.environ["STUDENT_SERVICE_URL"]
registrations = []


class RegistrationCreate(BaseModel):
    student_id: str
    course_name: str


@app.post("/registrations", status_code=201)
async def create_registration(registration: RegistrationCreate):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{STUDENT_SERVICE_URL}/students/{registration.student_id}",
                timeout=5,
            )
    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Student Service is unavailable",
        )

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Student not found")
    if response.is_error:
        raise HTTPException(
            status_code=502,
            detail="Student Service returned an error",
        )

    new_registration = {
        "registration_id": len(registrations) + 1,
        "student_id": registration.student_id,
        "course_name": registration.course_name,
    }
    registrations.append(new_registration)
    return new_registration


@app.get("/registrations")
async def get_registrations():
    return registrations
