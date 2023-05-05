import uuid
import typing as tp

from sqlmodel import SQLModel, Field, PrimaryKeyConstraint


class UserBase(SQLModel):
    name: tp.Optional[str] = None
    email: tp.Optional[str] = None
    bio: tp.Optional[str] = None
    password: tp.Optional[str] = None


class UserCreate(UserBase):
    pass


class Users(UserBase, table=True):
    id: uuid.UUID = Field(default=None, primary_key=True)


class FriendsBase(SQLModel):
    user_id: uuid.UUID
    friend_id: uuid.UUID


class FriendsCreate(FriendsBase):
    pass


class Friends(FriendsBase, table=True):
    __table_args__ = (PrimaryKeyConstraint("user_id", "friend_id"),)
