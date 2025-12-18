from fastapi import FastAPI
from app.api.search import router as search_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.favorites import router as favorites_router
from app.api.news import router as news_router

app = FastAPI(title="AI News Dashboard")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "AI News Dashboard Backend Running"}

# 🔑 THIS LINE WAS MISSING
app.include_router(search_router)
app.include_router(favorites_router)
app.include_router(news_router)


