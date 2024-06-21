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
    user_id: int = Field(
        ..., description="id of user that blog belongs to"
    )

