from fastapi import FastAPI, Cookie, Header, Response, HTTPException
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime, timedelta, timezone
from typing import Annotated

app = FastAPI()

class SessionCreate(BaseModel):
    user_id: UUID
    login_time: datetime
    expires_at: datetime
    permissions: frozenset[str]

@app.post("/sessions")
async def create_session(session: SessionCreate):
    return {
        "session_id": uuid4(),
        "user_id": session.user_id,
        "login_time": session.login_time,
        "expires_at": session.expires_at,
        "permissions": session.permissions
    }


@app.post("/session-cookie")
async def create_session_cookie(response: Response):
    session_id = str(uuid4())
    
    expire_time = datetime.now(timezone.utc) + timedelta(hours=1)
    
    response.set_cookie(
        key="session_id",
        value=session_id,
        expires=expire_time,
        max_age=3600,
        httponly=True
    )
    return {"message": "Session cookie created successfully!"}

@app.get("/session-cookie")
async def read_session_cookie(session_id: Annotated[str | None, Cookie()] = None):
    if not session_id:
        raise HTTPException(status_code=400, detail="Cookie does not exist")
    return {"session_id": session_id}


@app.get("/client-info")
async def get_client_info(
    x_client_version: Annotated[str | None, Header()] = None,
    x_request_id: Annotated[UUID | None, Header()] = None,
    user_agent: Annotated[str | None, Header()] = None
):
    return {
        "client_version": x_client_version,
        "request_id": x_request_id,
        "user_agent": user_agent
    }


class ActivityCreate(BaseModel):
    user_id: UUID
    activity_time: datetime
    actions: frozenset[str]

@app.post("/activities")
async def create_activity(
    activity: ActivityCreate,
    session_id: Annotated[str | None, Cookie()] = None,
    x_client_version: Annotated[str | None, Header()] = None,
    x_request_id: Annotated[UUID | None, Header()] = None
):
    return {
        "request_id": x_request_id,
        "session_id": session_id,
        "user_id": activity.user_id,
        "activity_time": activity.activity_time,
        "actions": activity.actions,
        "client_version": x_client_version
    }