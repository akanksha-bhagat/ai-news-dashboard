from datetime import datetime
from app.db import supabase

def log_broadcast(favorite_id, platform, status, message=None):
    supabase.table("broadcast_logs").insert({
        "favorite_id": favorite_id,
        "platform": platform,
        "status": status,
        "message": message
    }).execute()

def broadcast_email(favorite):
    subject = f"AI News: {favorite['title']}"
    body = f"""
    {favorite['title']}
    Source: {favorite.get('source')}
    Link: {favorite['url']}
    """

    # MOCK SEND
    print("EMAIL SENT")
    print(subject)
    print(body)

    log_broadcast(
        favorite_id=favorite["id"],
        platform="email",
        status="sent",
        message=subject
    )

def broadcast_linkedin(favorite):
    caption = f"""
🚀 AI Update:

{favorite['title']}

Why it matters 👇
{favorite.get('summary', '')[:200]}

🔗 {favorite['url']}
"""

    # MOCK POST
    print("LINKEDIN POST CREATED")
    print(caption)

    log_broadcast(
        favorite_id=favorite["id"],
        platform="linkedin",
        status="posted",
        message=caption[:200]
    )

def broadcast_whatsapp(favorite):
    message = f"""
AI News Alert 🤖

{favorite['title']}
{favorite['url']}
"""

    # MOCK SEND
    print("WHATSAPP MESSAGE SENT")
    print(message)

    log_broadcast(
        favorite_id=favorite["id"],
        platform="whatsapp",
        status="sent",
        message=message
    )

def broadcast_newsletter(favorite):
    print("NEWSLETTER PUBLISHED")
    print(f"""
    📰 AI NEWSLETTER ENTRY

    {favorite['title']}
    Source: {favorite['source']}
    Link: {favorite['url']}
    """)

    log_broadcast(
        favorite_id=favorite["id"],
        platform="newsletter",
        message=f"Newsletter published: {favorite['title']}"
    )
