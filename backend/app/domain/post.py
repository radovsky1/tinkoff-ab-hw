import uuid
from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Post:
    id: uuid.UUID
    author_id: uuid.UUID
    content: str
    created_at: datetime


@dataclass_json
@dataclass
class PostEvent:
    id: uuid.UUID
    author_id: uuid.UUID
