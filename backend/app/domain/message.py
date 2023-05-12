import uuid

from datetime import datetime
from dataclasses import dataclass


@dataclass
class Message:
    id: uuid.UUID
    sender_id: uuid.UUID
    receiver_id: uuid.UUID
    text: str
    created_at: datetime
