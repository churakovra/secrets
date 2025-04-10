import os
from dotenv import load_dotenv

load_dotenv()

LOCAL_ADDR = "0.0.0.0"
PG_PORT = "5432"

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{LOCAL_ADDR}:{PG_PORT}/postgres"
