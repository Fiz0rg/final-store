from passlib.context import CryptContext
from fastapi.security import SecurityScopes, OAuth2PasswordRequestForm, OAuth2PasswordBearer


SECRET_KEY = "7f18111e48f8b0f243bc48a2faa87e17541ceea805f094f11e07db807fccf337"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUNET = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token', scopes={"buyer": "just casual user"})
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(planed_password: str, hash_password: str):
    return pwd_context.verify(planed_password, hash_password)
