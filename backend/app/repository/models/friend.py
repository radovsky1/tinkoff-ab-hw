import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class Friend(Base):
    __tablename__ = 'friends'
    user_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
    )
    friend_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
    )
