from fastapi import APIRouter, Request
from typing import Optional
from app.schemas import User, Inventory, CreateUser
from app.models import UserLevel

router = APIRouter()

# http POST :8000/users name=spike password=password inventory:='[{"name": "무기3", "price": 10.0, "amount": 99}]'
@router.post("/users")
def create_user(user: CreateUser):
    return {
        "user_name": user.name,
        "password": user.password,
        "level": user.grade.value,
        "url": user.url,
        "inventory": user.inventory
    }

# http :8000/users/me

@router.get("/users/me", response_model=User)
async def get_current_user():
    fake_user = User(
        name="Test",
        grade=UserLevel.ADMIN,
        inventory=[
            Inventory(name="무기1", price=1_000_000, amount=1000000),
            Inventory(name="무기2", price=900_000, amount=900000)
        ]

    )
    return fake_user


@router.get("/users/params")
async def get_user_params(
    limit: int,
    level: Optional[int] = 10,
    is_admin: Optional[bool] = True
):
    return {
        "limit": limit,
        "level": level,
        "is_admin": is_admin
    }

@router.get("/users/class")
async def get_users(grade: UserLevel = UserLevel.NORMAL):
    return {
        "grade": grade.value,
    }

@router.get("/users/{user_id}")
async def get_users(user_id: int, request: Request):
    return {"user_id": user_id}
