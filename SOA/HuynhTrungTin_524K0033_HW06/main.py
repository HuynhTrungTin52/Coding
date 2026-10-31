from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, EmailStr
from typing import Annotated
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()
app = FastAPI()

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    full_name: str


USERS = [
    UserResponse(
        user_id=1,
        username="nguyenan",
        email="nguyen.an@example.com",
        full_name="Nguyen An",
    ),
    UserResponse(
        user_id=2,
        username="tranbinh",
        email="tran.binh@example.com",
        full_name="Tran Binh",
    ),
    UserResponse(
        user_id=3,
        username="lechi",
        email="le.chi@example.com",
        full_name="Le Chi",
    ),
]


@app.get("/v1/users", response_model=list[UserResponse])
def get_users() -> list[UserResponse]:
    return USERS

@app.get("/v1/users/{user_id}")
def get_user (
    user_id: Annotated[int, Path(title="The ID of the order to get", gt=0)]
):
    for user in USERS:
        if user.user_id==user_id:
            return user
    
    raise HTTPException(status_code=404, detail="User not found")


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    
class UserInput(UserBase):
    password: str
    
class UserOutput(UserBase):
    user_id: int
    
class UserInDb(UserBase):
    user_id: int
    hashed_password: str


def password_hasher(raw_password: str) -> str:
    return password_hash.hash(raw_password)


usersSaved: list[UserInDb] = [
    UserInDb(
        user_id=1,
        username="nguyenan",
        email="nguyen.an@example.com",
        full_name="Nguyen An",
        hashed_password=password_hasher("nguyenan123"),
    ),
    UserInDb(
        user_id=2,
        username="tranbinh",
        email="tran.binh@example.com",
        full_name="Tran Binh",
        hashed_password=password_hasher("tranbinh123"),
    ),
    UserInDb(
        user_id=3,
        username="lechi",
        email="le.chi@example.com",
        full_name="Le Chi",
        hashed_password=password_hasher("lechi123"),
    ),
]


@app.get("/v2/users", response_model=list[UserOutput])
def get_users() -> list[UserOutput]:
    return usersSaved

@app.get("/v2/users/{user_id}",response_model=UserOutput)
def get_user (
    user_id: Annotated[int, Path(title="The ID of the order to get", gt=0)]
):
    for user in usersSaved:
        if user.user_id==user_id:
            return user
    
    raise HTTPException(status_code=404, detail="User not found")

def save_user(user_in: UserInput):
    hashed_password = password_hasher(user_in.password)
    new_id=len(usersSaved)+1
    user_db = UserInDb(**user_in.model_dump(), hashed_password=hashed_password, user_id=new_id)
    print("User has been saved to an imaginary database!")
    print(user_db)
    usersSaved.append(user_db)
    return user_db

@app.post("/v2/user", response_model=UserOutput)
def create_user(user: UserInput):
    user_saved = save_user(user)
    return user_saved