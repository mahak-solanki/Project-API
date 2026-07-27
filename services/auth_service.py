from sqlalchemy.orm import Session

from models.user import User
from schemas.auth import UserRegister, UserLogin
from repositories.user_repository import (
    create_user,
    get_user_by_email
)
from core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(
    db: Session,
    user_data: UserRegister
):

    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise ValueError("User already exists.")

    hashed_password = hash_password(
        user_data.password
    )

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )

    return create_user(
        db,
        new_user
    )


def login_user(
    db: Session,
    email: str,
    password: str
):

    user = get_user_by_email(
    db,
    email
)

    if not user:
        raise ValueError(
            "Invalid Email or Password."
        )

    if not verify_password(
        password,
        user.hashed_password
    ):
        raise ValueError(
            "Invalid Email or Password."
        )

    access_token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }