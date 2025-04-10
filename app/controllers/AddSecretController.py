from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.Secret import Secret

add_secret_router = APIRouter()


@add_secret_router.post("/secret")
async def add_secret(secret: Secret, db: Session = Depends(get_db)):
    new_secret = Secret(secret=secret.secret)
    db.add(new_secret)
    db.commit()
    db.refresh(new_secret)
