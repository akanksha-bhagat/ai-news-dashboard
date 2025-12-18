# backend/app/ingest_news.py

import asyncio
import feedparser
from sqlalchemy import select

from app.db import AsyncSessionLocal
from app.models import Source, NewsItem
from app.sources import SOURCES


MAX_ENTRIES_PER_SOURCE = 50  # IMPORTANT: prevent huge feeds from blocking


async def get_or_create_source(session, name: str, url: str) -> Source:
    """Fetch source if exists, else create it."""
    result = await session.execute(
        select(Source).where(Source.name == name)
    )
    source = result.scalar_one_or_none()

    if source:
        return source

    source = Source(name=name, url=url)
    session.add(source)
    await session.commit()
    await session.refresh(source)
    return source


async def ingest_news():
    async with AsyncSessionLocal() as session:
        for src in SOURCES:
            print(f"\n🔎 Fetching: {src['name']}")

            # Ensure source exists
            source = await get_or_create_source(
                session,
                src["name"],
                src["url"],
            )

            # Parse RSS / feed
            feed = feedparser.parse(src["url"])
            total_entries = len(feed.entries)
            print(f"📰 entries found: {total_entries}")

            if total_entries == 0:
                continue

            inserted = 0

            for i, entry in enumerate(
                feed.entries[:MAX_ENTRIES_PER_SOURCE],
                start=1
            ):
                print(
                    f"   → Processing entry {i}/{min(MAX_ENTRIES_PER_SOURCE, total_entries)}",
                    end="\r",
                )

                link = entry.get("link")
                title = entry.get("title", "").strip()
                summary = entry.get("summary", "").strip()

                if not link:
                    continue

                # Deduplication
                exists = await session.execute(
                    select(NewsItem).where(NewsItem.url == link)
                )
                if exists.scalar_one_or_none():
                    continue

                news = NewsItem(
                    title=title,
                    url=link,
                    summary=summary,
                    source_id=source.id,
                )

                session.add(news)
                inserted += 1

            await session.commit()
            print(f"\n✅ Inserted {inserted} new articles from {src['name']}")

    print("\n🎉 News ingestion completed successfully.")


if __name__ == "__main__":
    asyncio.run(ingest_news())
