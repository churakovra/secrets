from typing import Optional

from pydantic import BaseModel


class Secret(BaseModel):
    secret: str
    passphrase: Optional[str] = None
    ttl_seconds: Optional[int] = None

    class Config:
        orm_mode = True
