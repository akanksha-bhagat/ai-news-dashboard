import feedparser
from datetime import datetime


def fetch_feed_entries(feed_url: str, limit: int = 50):
    """
    Parse RSS/Atom feed and return normalized entries
    """
    feed = feedparser.parse(feed_url)

    entries = []
    for entry in feed.entries[:limit]:
        entries.append({
            "title": entry.get("title", "").strip(),
            "url": entry.get("link"),
            "content": entry.get("summary", "").strip(),
            "published_at": _parse_date(entry),
        })

    return entries


def _parse_date(entry):
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        return datetime(*entry.published_parsed[:6])
    return None


def to_pgvector(vec: list[float]) -> str:
    """
    Convert embedding list → pgvector string
    """
    return "[" + ",".join(str(x) for x in vec) + "]"
