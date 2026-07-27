from fastapi import APIRouter, Depends , status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schemas.auth import UserRegister, TokenResponse
from services.auth_service import register_user, login_user
from dependencies.database import get_db

#router object
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

#register router API
@router.post("/register" , status_code=status.HTTP_201_CREATED,
             summary= "Register new user",
             description= "Creates a new user account with username , email and password",
             response_description="User registered successfully.")
def signup(user: UserRegister, db: Session = Depends(get_db)):

    new_user = register_user(db , user )

    return {
        "message": "User Registered Successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    }


#login router   
@router.post("/login", response_model=TokenResponse,
                 summary="User Login",
                 description="Authenticates a user and returns a JWT access token.",
                  response_description="JWT Access Token.")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    return login_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )