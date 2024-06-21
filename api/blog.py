from fastapi import APIRouter
from schemas import BlogPost, UserBase, UserIn, UserOut

router = APIRouter()


@router.get("/")
def blogs():
    pass


@router.get("/{id}")
def blog(id: int):
    pass


@router.post("/")
def create_blog():
    pass


@router.put("/{id}")
def update_blog(id: int):
    pass


@router.delete("/{id}")
def delete_blog(id: int):
    pass


