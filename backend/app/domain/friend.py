import uuid
from dataclasses import dataclass


@dataclass
class Friend:
    user_id: uuid.UUID
    friend_id: uuid.UUID
