from sqlalchemy.orm import Session

from . import models
import schemas


def get_user(db: Session, user_id: int) -> schemas.User:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


def get_user_by_email(db: Session, email: str) -> schemas.User:
    user = db.query(models.User).filter(models.User.email == email).first()
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


def create_user(db: Session, user: schemas.UserCreate):
    hash_password = None
    new_user = models.User(login=user.login, email=user.email, hashed_password=hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    blogs = db.query(models.Blog).offset(skip).limit(limit)
    return blogs


def get_user_blogs(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user.blogs


def create_blog(db: Session, blog: schemas.BlogPostBase, user_id: int):
    blog = models.Blog(**blog.dict(), user_id=user_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog






