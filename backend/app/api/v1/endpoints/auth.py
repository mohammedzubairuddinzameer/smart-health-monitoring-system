from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.auth.hashing import hash_password
from app.models.user import User
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = get_user_by_email(
        db,
        user.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role,
    )

    return create_user(
        db,
        db_user,
    )