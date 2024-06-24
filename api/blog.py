from fastapi import APIRouter, Depends, HTTPException
import schemas
from sqlalchemy.orm import Session

from sql_app import crud, database

router = APIRouter()


@router.get("/")
def read_blogs(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    blogs = crud.get_blogs(db, skip, limit)
    return blogs


@router.get("/{user_id}")
def read_blog(user_id: int, db: Session = Depends(database.get_db)):
    blog = crud.get_user_blogs(db, user_id=user_id)
    if blog is None:
        return {"message": "no blogs yet"}
    return blog


@router.post("/{user_id}")
def create_blog(
    user_id: int, blog: schemas.BlogPostCreate, db: Session = Depends(database.get_db)
):
    new_blog = crud.create_blog(blog=blog, db=db, user_id=user_id)
    return new_blog


@router.put("/{id}")
def update_blog(id: int):
    pass


@router.delete("/{id}")
def delete_blog(id: int):
    pass


