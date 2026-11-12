import importlib
import sys
from pathlib import Path

import httpx2
import pytest
from fastapi.testclient import TestClient

#pytest tests/test_integration.py
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


@pytest.fixture
def services(monkeypatch):
    doctor = importlib.import_module("doctor_service.main")
    notification = importlib.import_module("notification_service.main")
    booking = importlib.import_module("booking_service.main")
    booking.bookings.clear()
    monkeypatch.setattr(booking, "DOCTOR_SERVICE_URL", "http://doctor.test")
    monkeypatch.setattr(booking, "NOTIFICATION_SERVICE_URL", "http://notification.test")

    real_get = httpx2.get
    real_post = httpx2.post

    def get(url, **kwargs):
        if url.startswith("http://doctor.test"):
            client = TestClient(doctor.app)
            response = client.get(url.removeprefix("http://doctor.test"))
            return httpx2.Response(
                response.status_code, json=response.json(), request=httpx2.Request("GET", url)
            )
        return real_get(url, **kwargs)

    def post(url, **kwargs):
        if url.startswith("http://notification.test"):
            client = TestClient(notification.app)
            response = client.post(
                url.removeprefix("http://notification.test"), json=kwargs["json"]
            )
            return httpx2.Response(
                response.status_code, json=response.json(), request=httpx2.Request("POST", url)
            )
        return real_post(url, **kwargs)

    monkeypatch.setattr(httpx2, "get", get)
    monkeypatch.setattr(httpx2, "post", post)
    return TestClient(booking.app), booking


def payload(**changes):
    data = {
        "patient_name": "Huynh Trung Tin",
        "email": "Tin@example.com",
        "doctor_id": 2,
        "appointment_time": "2026-11-12 10:00"
    }
    data.update(changes)
    return data


def test_available_doctor_creates_booking_and_notification(services):
    client, _ = services
    response = client.post("/bookings", json=payload())

    assert response.status_code == 200
    assert response.json()["notification_status"] == "sent"


def test_missing_doctor_is_rejected(services):
    client, _ = services
    response = client.post("/bookings", json=payload(doctor_id=99))

    assert response.status_code == 404
    assert response.json()["detail"] == "Doctor not found"


def test_unavailable_doctor_is_rejected(services):
    client, _ = services
    response = client.post(
        "/bookings", json=payload(appointment_time="2026-11-12 11:00")
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Doctor is unavailable"


def test_doctor_service_failure_is_reported(services, monkeypatch):
    client, booking = services

    def fail(*args, **kwargs):
        raise httpx2.ConnectError("doctor is down")

    monkeypatch.setattr(httpx2, "get", fail)
    response = client.post("/bookings", json=payload())

    assert response.status_code == 503
    assert response.json()["detail"] == "Doctor Service is unavailable"
    assert booking.bookings == []


def test_notification_failure_does_not_cancel_booking(services, monkeypatch):
    client, booking = services

    def fail(*args, **kwargs):
        raise httpx2.ConnectError("notification is down")

    monkeypatch.setattr(httpx2, "post", fail)
    response = client.post("/bookings", json=payload())

    assert response.status_code == 200
    assert response.json()["notification_status"] == "failed"
    assert len(booking.bookings) == 1
