from sqlalchemy import Column, Integer, String, Text, Boolean, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from .db import Base

class Source(Base):
    __tablename__ = "sources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    url = Column(String)
    type = Column(String)
    active = Column(Boolean, default=True)

class NewsItem(Base):
    __tablename__ = "news_items"
    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=True)
    title = Column(String, nullable=False)
    summary = Column(Text)
    url = Column(String, unique=True)
    published_at = Column(TIMESTAMP(timezone=True), default=func.now())
    tags = Column(JSON, default=[])
    is_duplicate = Column(Boolean, default=False)
    # embedding vector column — adjust dim to match your embedding model (e.g., 384)
    embedding = Column(Vector(384), nullable=True)
    canonical_id = Column(Integer, nullable=True)

    source = relationship("Source", backref="news_items")

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    news_item_id = Column(Integer, ForeignKey("news_items.id"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())

class BroadcastLog(Base):
    __tablename__ = "broadcast_logs"
    id = Column(Integer, primary_key=True, index=True)
    favorite_id = Column(Integer, ForeignKey("favorites.id"), nullable=True)
    platform = Column(String)  # email, linkedin, whatsapp, newsletter
    status = Column(String)
    timestamp = Column(TIMESTAMP(timezone=True), default=func.now())

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String, default="user")
