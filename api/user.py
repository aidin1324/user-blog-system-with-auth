from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import User, UserCreate
from sql_app import database, crud

router = APIRouter(tags=["user"])


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(404, detail="user already exists")
    return crud.create_user(user=user, db=db)


@router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.get_user(user_id=user_id, db=db)
    if user is None:
        raise HTTPException(404, detail="User not found")
    return user
