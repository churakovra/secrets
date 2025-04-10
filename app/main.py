from fastapi import FastAPI
from app.controllers.AddSecretController import add_secret_router

app = FastAPI()

app.include_router(add_secret_router, prefix="/")