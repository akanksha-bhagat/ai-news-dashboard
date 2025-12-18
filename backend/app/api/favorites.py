from fastapi import APIRouter
from app.db import supabase

from app.broadcast import (
    broadcast_email,
    broadcast_linkedin,
    broadcast_whatsapp,
    broadcast_newsletter   
)


router = APIRouter(prefix="/favorites", tags=["Favorites"])


# ✅ ADD FAVORITE
@router.post("")
def add_favorite(
    title: str,
    url: str,
    source: str | None = None,
):
    response = (
        supabase
        .table("favorites")
        .insert({
            "title": title,
            "url": url,
            "source": source
        })
        .execute()
    )

    return {
        "status": "saved",
        "id": response.data[0]["id"]
    }


# ✅ GET FAVORITES
@router.get("")
def get_favorites():
    response = (
        supabase
        .table("favorites")
        .select("id, title, url, source, created_at")
        .order("created_at", desc=True)
        .execute()
    )

    return response.data


# ✅ BROADCAST FAVORITE
@router.post("/{favorite_id}/broadcast/{platform}")
def broadcast_favorite(favorite_id: int, platform: str):
    favorite = (
        supabase
        .table("favorites")
        .select("*")
        .eq("id", favorite_id)
        .single()
        .execute()
        .data
    )

    if not favorite:
        return {"error": "Favorite not found"}

    if platform == "email":
        broadcast_email(favorite)
    elif platform == "linkedin":
        broadcast_linkedin(favorite)
    elif platform == "whatsapp":
        broadcast_whatsapp(favorite)
    else:
        return {"error": "Unsupported platform"}

    return {
        "status": "broadcasted",
        "platform": platform
    }
