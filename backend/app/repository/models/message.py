import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func, text

from .base import Base


class Message(Base):
    __tablename__ = 'messages'
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
    )
    sender_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    receiver_id = Column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        nullable=False,
    )
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


Index(
    'messages_id_sender_id_created_at_desc_idx',
    Message.id,
    Message.sender_id,
    Message.created_at.desc(),
)

Index(
    'messages_text_trgm_idx',
    Message.text,
    postgresql_using='gin',
    postgresql_ops={
        'description': 'gin_trgm_ops',
    },
)

Index(
    'messages_text_ts_idx',
    func.to_tsvector('russian', text('text')),
    postgresql_using='gin',
)
