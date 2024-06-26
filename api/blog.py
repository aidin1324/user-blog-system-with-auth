from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError

import schemas
from sqlalchemy.orm import Session

from sql_app import crud, database, models

router = APIRouter(tags=["blogs"])


@router.get("/")
def read_blogs(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    blogs = crud.get_blogs(db, skip, limit)
    return blogs


@router.post("/{user_id}")
def create_blog(
    user_id: int, blog: schemas.BlogPostCreate, db: Session = Depends(database.get_db)
):
    try:
        new_blog = crud.create_blog(blog=blog, db=db, user_id=user_id)
    except SQLAlchemyError as e:
        return HTTPException(status_code=500, detail=str(e))
    return new_blog


@router.put("/{item_id}", response_model=schemas.BlogPost)
def update_blog(blog_id: int, blog: schemas.BlogPostUpdate, db: Session = Depends(database.get_db)):
    blog = crud.update_blog(db=db, blog_id=blog_id, blog_update=blog)
    if blog is None:
        return HTTPException(404, "Blog not found")
    return blog


@router.delete("/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(database.get_db)):
    result = crud.delete_blog(blog_id=blog_id, db=db)
    if result is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return result

