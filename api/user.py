from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import User, UserCreate
from sql_app import database, crud

router = APIRouter()


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(user=user, db=db)


@router.get("/", response_model=list[User])
def read_user(db: Session = Depends(database.get_db)):
    return crud.get_users(db=db)

