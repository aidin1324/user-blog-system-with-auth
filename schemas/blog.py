from pydantic import BaseModel, Field

from typing import Union


class BlogPostBase(BaseModel):
    title: str = Field(
        ..., max_length=50,
        description="Title of blog, max 50 characters"
    )

    content: str = Field(
        description="Content of blog"
    )

class BlogPostCreate(BlogPostBase):
    pass


class BlogPostUpdate(BlogPostBase):
    title: Union[str, None] = None
    content: Union[str, None] = None


class BlogPost(BlogPostBase):
    id: int = Field(
        ..., description="Blog id"
    )
    user_id: int = Field(
        ..., description="id of user that blog belongs to"
    )

    class Config:
        orm_mode = True