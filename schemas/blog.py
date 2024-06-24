from pydantic import BaseModel, Field


class BlogPostBase(BaseModel):
    title: str = Field(
        ..., max_length=50,
        description="Title of blog, max 50 characters"
    )

    content: str = Field(
        description="Content of blog"
    )


class BlogPost(BlogPostBase):
    id: int = Field(
        ..., description="Blog id"
    )
    user_id: int = Field(
        ..., description="id of user that blog belongs to"
    )

    class Config:
        orm_mode = True