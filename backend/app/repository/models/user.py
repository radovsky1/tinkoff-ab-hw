import datetime
import uuid

from sqlalchemy import Column, String, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
    )
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    bio = Column(String, nullable=True)
    password = Column(String, nullable=False)
    last_login = Column(DateTime, default=datetime.datetime.utcnow)


Index(
    'users_id_name_last_login_desc_idx',
    User.id,
    User.name,
    User.last_login.desc(),
)

Index(
    'users_name_trgm_idx',
    User.name,
    postgresql_using='gin',
    postgresql_ops={
        'name': 'gin_trgm_ops',
    }
)

Index(
    'users_name_text_pattern_ops_idx',
    User.name,
    postgresql_ops={
        'name': 'text_pattern_ops',
    }
)
