from fastapi import FastAPI

from sql_app import models, database
from sql_app.database import engine
from api import blog, user, auth
models.Base.metadata.create_all(engine)

app = FastAPI()


app.include_router(user.router, prefix="/users")
app.include_router(blog.router, prefix="/items")
app.include_router(auth.router)