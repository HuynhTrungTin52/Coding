import logging

from fastapi import FastAPI
from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Notification Service")


class Notification(BaseModel):
    recipient: str
    subject: str
    message: str


@app.post("/notifications")
def send_notification(notification: Notification):
    logging.info("Sending confirmation to %s", notification.recipient)
    return {"status": "sent", "recipient": notification.recipient}
