from sqlmodel import select
from bot.models import User, Group
from bot.database import session_scope


async def add_user(user_id: int, username: str | None):
    async with session_scope() as s:
        if not await s.get(User, user_id):
            s.add(User(id=user_id, username=username))


async def new_group(name: str):
    async with session_scope() as s:
        if not (await s.exec(select(Group).where(Group.name == name))).first():
            s.add(Group(name=name))
