import logging

from fastapi import FastAPI, HTTPException


logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Doctor Service")

doctors = [
    {
        "doctor_id": 1,
        "name": "Dr. Nguyen Van An",
        "specialty": "Cardiology",
        "available_slots": ["2026-11-12 09:00", "2026-11-12 14:00"],
    },
    {
        "doctor_id": 2,
        "name": "Dr. Tran Thi Binh",
        "specialty": "Dermatology",
        "available_slots": ["2026-11-12 10:00", "2026-11-13 15:00"],
    },
    {
        "doctor_id": 3,
        "name": "Dr. Le Minh Chau",
        "specialty": "Pediatrics",
        "available_slots": ["2026-11-14 08:30", "2026-11-14 13:30"],
    },
]


@app.get("/doctors")
def get_doctors():
    logging.info("Returning all doctors")
    return doctors


@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor["doctor_id"] == doctor_id:
            logging.info("Returning doctor %s", doctor_id)
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")
