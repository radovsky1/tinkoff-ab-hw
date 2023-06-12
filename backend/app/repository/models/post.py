import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
    )
    author_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
