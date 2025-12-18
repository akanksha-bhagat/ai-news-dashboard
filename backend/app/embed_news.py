import asyncio
from sqlalchemy import select
from sentence_transformers import SentenceTransformer
from app.db import AsyncSessionLocal
from app.models import NewsItem

model = SentenceTransformer("all-MiniLM-L6-v2")

async def embed_news(batch_size: int = 50):
    print("🚀 Starting embedding job")

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(NewsItem).where(NewsItem.embedding == None)
        )
        news_items = result.scalars().all()

        print(f"📰 Found {len(news_items)} items to embed")

        for i, news in enumerate(news_items, start=1):
            text = f"{news.title}\n{news.summary or ''}".strip()

            if not text:
                continue

            embedding = model.encode(text).tolist()
            news.embedding = embedding

            if i % batch_size == 0:
                await session.commit()
                print(f"✅ Embedded {i} items")

        await session.commit()
        print("🎉 Embedding completed")

if __name__ == "__main__":
    asyncio.run(embed_news())
