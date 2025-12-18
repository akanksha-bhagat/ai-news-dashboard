from fastapi import APIRouter
from app.db import supabase

router = APIRouter(prefix="/news", tags=["News"])

@router.get("")
def get_latest_news(limit: int = 20):
    response = (
        supabase
        .table("news_items")
        .select(
            "id, title, url, published_at, sources(name)"
        )
        .order("published_at", desc=True)
        .limit(limit)
        .execute()
    )

    return [
        {
            "id": item["id"],
            "title": item["title"],
            "url": item["url"],
            "published_at": item["published_at"],
            "source": item["sources"]["name"] if item.get("sources") else None,
        }
        for item in response.data
    ]
