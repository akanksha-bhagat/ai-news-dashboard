from fastapi import APIRouter, HTTPException
from app.db import supabase
from app.embeddings import embed_text

router = APIRouter()

@router.get("/search")
def search_news(q: str):
    # 1. Check if embeddings exist
    check = (
        supabase
        .table("news_items")
        .select("id")
        .not_.is_("embedding", None)
        .limit(1)
        .execute()
    )

    if not check.data:
        return {
            "message": "No embeddings found yet. Run embedding generation first.",
            "results": []
        }

    # 2. Generate embedding
    embedding = embed_text(q)
    embedding_str = "[" + ",".join(f"{x:.6f}" for x in embedding) + "]"
    
    query = f"""
    SELECT
        n.title::text AS title,
        n.url::text AS url,
        s.name::text AS source,
        1 - (n.embedding <=> '{embedding_str}'::vector) AS similarity
    FROM news_items n
    JOIN sources s ON n.source_id = s.id
    WHERE n.embedding IS NOT NULL
    ORDER BY n.embedding <=> '{embedding_str}'::vector
    LIMIT 10;
"""

    response = supabase.rpc("execute_sql", {"sql": query}).execute()
    return response.data
