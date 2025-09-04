from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import Annotated
from fastapi import Depends
from model import TokenModel

URL_LINK_DATABASE = 'sqlalchemy+aiosqlite:///./tokens.db'
engine = create_async_engine(url=URL_LINK_DATABASE)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_session():
    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]