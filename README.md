# 🧠 AI News Dashboard

AI News Dashboard is an end-to-end AI-focused news aggregation platform that collects the latest AI-related news from multiple trusted sources, enables semantic search, allows users to save important articles, and broadcast them across multiple channels.

I built this project as a complete, production-style MVP to demonstrate backend API design, semantic search using embeddings, frontend dashboards, and extensible broadcast workflows.

---

## 🚀 Key Features

### 📰 AI News Aggregation
- Aggregates AI news from multiple sources such as OpenAI, Google AI, Meta AI, TechCrunch, MIT Technology Review, and more
- Normalizes and stores articles in a PostgreSQL database (Supabase)

### 🔍 Semantic Search
- Supports embedding-based semantic search using `pgvector`
- Returns contextually relevant AI news instead of simple keyword matches

### ⭐ Favorites Management
- Save important news articles to favorites
- View and manage saved articles in a dedicated Favorites dashboard

### 📣 Multi-Channel Broadcasting
- Broadcast favorite articles to multiple platforms:
  - 📧 Email
  - 💼 LinkedIn
  - 💬 WhatsApp
  - 📰 Newsletter
- All broadcasts are logged for traceability and analytics

> Note: External broadcasting services are mocked for MVP purposes and can be easily replaced with real integrations such as Mailchimp, LinkedIn API, or Twilio.

---

## 🏗️ System Architecture

The system follows a clean three-layer architecture:

Frontend (Next.js)
│
│ Search • Browse • Favorites • Broadcast
│
▼
Backend (FastAPI)
│
├── /news → Latest AI news feed
├── /search → Semantic search using embeddings
├── /favorites → Save & retrieve favorite articles
└── /broadcast → Multi-channel broadcasting
│
▼
Database (Supabase PostgreSQL)
│
├── sources
├── news_items (with vector embeddings)
├── favorites
└── broadcast_logs

---

## 🧰 Tech Stack

### Frontend
- Next.js (App Router)
- TypeScript
- Fetch API

### Backend
- FastAPI
- Python
- Supabase Python Client
- pgvector for semantic search

### Database
- PostgreSQL (Supabase)
- pgvector extension

---

## 📂 Project Structure
ai-news-dashboard/
│
├── backend/
│ ├── app/
│ │ ├── api/
│ │ │ ├── news.py
│ │ │ ├── search.py
│ │ │ └── favorites.py
│ │ ├── broadcast.py
│ │ ├── db.py
│ │ └── main.py
│ ├── requirements.txt
│ └── .env # not committed
│
├── frontend/
│ ├── app/
│ │ ├── page.tsx
│ │ └── favorites/page.tsx
│ ├── package.json
│ └── .env.local # not committed
│
├── .gitignore
└── README.md

---

## ⚙️ Setup Instructions

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

### Frontend Setup
cd frontend
npm install
npm run dev

🔐 Environment Variables
Backend (backend/.env)
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

Frontend (frontend/.env.local)
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000

🧪 Example User Flow

Browse the latest AI news on the dashboard

Search semantically (e.g., “OpenAI new model”)

Save relevant articles as favorites ⭐

Broadcast selected articles via Email, LinkedIn, WhatsApp, or Newsletter

View broadcast logs in the database

📈 Future Enhancements

Real third-party integrations (Mailchimp, LinkedIn API, Twilio)

User authentication and personalization

Scheduled AI news digests

Analytics dashboard for engagement tracking

---

