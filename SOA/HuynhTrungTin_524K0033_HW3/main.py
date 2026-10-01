from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pwdlib import PasswordHash
from pydantic import BaseModel, Field

app = FastAPI()

tasks = [
    {
        "task_id": 1,
        "title": "Prepare lecture slides",
        "description": "Prepare slides for the SOA course",
        "priority": 5,
        "completed": False,
    },
    {
        "task_id": 2,
        "title": "Review student submissions",
        "description": "Review Lab 2 submissions",
        "priority": 4,
        "completed": True,
    },
    {
        "task_id": 3,
        "title": "Update course website",
        "description": "Update learning materials",
        "priority": 3,
        "completed": False,
    },
]


@app.get("/tasks")
def return_tasks(
    priority: int | None = None, completed: bool | None = None, limit: int | None = None
):
    if priority:
        return [task for task in tasks if task["priority"] == priority]

    if completed is not None:
        return [task for task in tasks if task["completed"] == completed]

    if limit:
        return tasks[:limit]

    return tasks


@app.get("/tasks/{task_id}")
async def return_task_id(task_id: int):
    is_task = next((task for task in tasks if task["task_id"] == task_id), None)
    if is_task == None:
        # print(type(tasks[1]["task_id"])==type(task_id))
        raise HTTPException(status_code=404, detail="task not found")

    return is_task


SECRET_KEY = "I-Havent-Sleep-Last-Night"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120
pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

user = {"username": "admin", "password": pwd_context.hash("admin123")}


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Creates a new JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    """
    Takes username and password from a form and returns a JWT token.
    """
    if form_data.username != user["username"] or not pwd_context.verify(
        form_data.password, user["password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3)
    description: str | None = None
    priority: int = Field(..., ge=1, le=5)
    completed: bool

async def get_current_active_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Decodes the JWT token to get the current user.
    This function acts as a dependency for protected endpoints.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # Get user from the 'database'
    return username

@app.post("/tasks")
async def create_task(
    task: TaskCreate, 
    current_user: Annotated[str, Depends(get_current_active_user)]
):

    new_task_id = max((t["task_id"] for t in tasks), default=0) + 1
    
    new_task = {
        "task_id": new_task_id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "completed": task.completed
    }
    
    tasks.append(new_task)
    
    return new_task