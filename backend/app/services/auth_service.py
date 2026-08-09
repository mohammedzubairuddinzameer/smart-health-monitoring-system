from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.auth.hashing import PasswordHasher
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    def register(user_data, db: Session):
        try:
            if UserRepository.get_by_email(db, user_data.email):
                raise HTTPException(
                    status_code=400,
                    detail="Email already exists",
                )

            user = User(
                name=user_data.name,
                email=user_data.email,
                hashed_password=PasswordHasher.hash(user_data.password),
                role=user_data.role,
            )

            return UserRepository.create(db, user)

        except Exception as e:
            print("=" * 80)
            print(type(e))
            print(e)
            print("=" * 80)
            raise