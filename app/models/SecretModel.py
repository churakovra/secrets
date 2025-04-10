from sqlalchemy import Column, Integer, String, TIMESTAMP
from app.database import Base


class Secret(Base):
    __tablename__ = "secrets_test"

    value = Column(String, index=True)
    passphrase = Column(String, index=True)
    ttl_seconds = Column(String, index=True)
