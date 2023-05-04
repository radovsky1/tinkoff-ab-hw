import uuid
from dataclasses import dataclass


@dataclass
class User:
    id: uuid.UUID | None
    name: str
    email: str
    bio: str
    password: str
