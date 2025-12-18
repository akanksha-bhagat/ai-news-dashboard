import asyncio
from app.db import engine, Base
from app.models import Source, NewsItem


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created successfully")


if __name__ == "__main__":
    asyncio.run(create_tables())
