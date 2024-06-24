from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm

from sql_app import database, models
from sqlalchemy.orm import Session

import schemas
from utils import utils
from oauth2 import oauth2

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=schemas.Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):

    user = db.query(models.User).filter(
        models.User.email == user_credentials.username
    ).first()

    if user is None:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not utils.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Incorrect password or login")

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
