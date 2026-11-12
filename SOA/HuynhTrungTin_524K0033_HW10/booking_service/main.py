import logging
import os
from datetime import datetime

import httpx2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Booking Service")

DOCTOR_SERVICE_URL = os.getenv("DOCTOR_SERVICE_URL", "http://127.0.0.1:8000")
NOTIFICATION_SERVICE_URL = os.getenv(
    "NOTIFICATION_SERVICE_URL", "http://127.0.0.1:8002"
)
bookings = []


class BookingCreate(BaseModel):
    patient_name: str
    email: str
    doctor_id: int
    appointment_time: str


def new_id():
    return len(bookings) + 1


@app.post("/bookings")
def create_booking(data: BookingCreate):
    try:
        doctor_response = httpx2.get(
            f"{DOCTOR_SERVICE_URL}/doctors/{data.doctor_id}", timeout=3.0
        )
    except httpx2.RequestError:
        logging.error("Doctor Service is unavailable")
        raise HTTPException(status_code=503, detail="Doctor Service is unavailable")

    if doctor_response.status_code == 404:
        raise HTTPException(status_code=404, detail="Doctor not found")
    if doctor_response.status_code != 200:
        raise HTTPException(status_code=502, detail="Doctor Service failed")

    doctor = doctor_response.json()
    if data.appointment_time not in doctor["available_slots"]:
        raise HTTPException(status_code=409, detail="Doctor is unavailable")

    booking = {
        "booking_id": new_id(),
        "patient_name": data.patient_name,
        "email": data.email,
        "doctor_id": data.doctor_id,
        "doctor_name": doctor["name"],
        "appointment_time": data.appointment_time,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    bookings.append(booking)
    logging.info("Created booking %s", booking["booking_id"])

    notification = {
        "recipient": data.email,
        "subject": "Appointment Confirmation",
        "message": (
            f"Your appointment with {doctor['name']} on "
            f"{data.appointment_time} has been booked."
        ),
    }
    notification_status = "failed"
    try:
        notification_response = httpx2.post(
            f"{NOTIFICATION_SERVICE_URL}/notifications",
            json=notification,
            timeout=3.0,
        )
        if notification_response.status_code == 200:
            notification_status = notification_response.json().get("status", "sent")
        else:
            logging.error("Notification Service returned %s", notification_response.status_code)
    except httpx2.RequestError:
        logging.error("Notification Service is unavailable")

    return {"booking": booking, "notification_status": notification_status}


@app.get("/bookings")
def get_bookings():
    return bookings
