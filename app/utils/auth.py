import uuid
from datetime import datetime, timedelta
from typing import Union

# jwt
from jose import JWTError, jwt
from passlib.context import CryptContext
from passlib.hash import pbkdf2_sha256

# config
from app.config import config

SECRET_KEY = config.SECRET_KEY
ALGORITHM = "SHA256"

#
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str):
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    subject: str,
    token_type: str = "access",
    expire_minutes: int = 15,
):
    """Creates an access token."""
    iat = datetime.utcnow()
    nbf = datetime.utcnow()
    exp = datetime.utcnow() + timedelta(minutes=expire_minutes)
    jti = str(uuid.uuid4())
    data = {
        "sub": subject,
        "type": token_type,
        "iat": iat,
        "nbf": nbf,
        "jti": jti,
        "exp": exp,
    }

    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> dict:
    """decodes an access token."""
    data = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    return data


def token_has_expired(token: dict):
    """Checks if a token has expired."""
    expiration = token.get("exp")
    expiration_date = datetime.fromtimestamp(expiration)
    now = datetime.now()
    return expiration_date < now


def decode_and_verify_token(token: Union[str, dict]):
    """Decodes a token an verifies if it has expired."""
    if isinstance(token, str):
        token = decode_access_token(token)
    if token_has_expired(token):
        raise ValueError("Token has expired")
    return token
