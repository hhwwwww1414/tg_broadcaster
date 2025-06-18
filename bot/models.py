from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class GroupUser(SQLModel, table=True):
    group_id: Optional[int] = Field(default=None, foreign_key="group.id", primary_key=True)
    user_id:  Optional[int] = Field(default=None, foreign_key="user.id",  primary_key=True)


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)               # Telegram-ID
    username: Optional[str]

    groups: List["Group"] = Relationship(back_populates="users", link_model=GroupUser)


class Group(SQLModel, table=True):
    id:   Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    users: List[User] = Relationship(back_populates="groups", link_model=GroupUser)
