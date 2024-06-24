import os
from dotenv import load_dotenv

# hash and check password
from passlib.context import CryptContext

# work with jwt token
from jose import JWTError, jwt

# work with time
from datetime import datetime, timedelta

path = "../../.env"
load_dotenv(path)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


