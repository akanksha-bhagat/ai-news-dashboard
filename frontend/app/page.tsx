"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

type NewsItem = {
  id: number;
  title: string;
  url: string;
  source: string | null;
  published_at: string;
};

export default function HomePage() {
  const [news, setNews] = useState<NewsItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [query, setQuery] = useState("");

  const router = useRouter();
  const API = process.env.NEXT_PUBLIC_API_URL;

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const res = await fetch(`${API}/news?limit=25`);
        const data = await res.json();
        setNews(data);
      } catch (e) {
        console.error("Failed to load news", e);
      } finally {
        setLoading(false);
      }
    };

    fetchNews();
  }, []);
  const addToFavorites = async (item: NewsItem) => {
  try {
    await fetch(
      `${API}/favorites?title=${encodeURIComponent(item.title)}&url=${encodeURIComponent(item.url)}&source=${encodeURIComponent(item.source ?? "")}`,
      { method: "POST" }
    );

    alert("⭐ Added to favorites!");
  } catch (err) {
    console.error(err);
    alert("Failed to add favorite");
  }
  };


  const handleSearch = () => {
    if (!query.trim()) return;
    router.push(`/search?q=${encodeURIComponent(query)}`);
  };

  return (
    <main className="p-6 max-w-5xl mx-auto">
  

      {/* 🔍 SEARCH BAR */}
      <div className="flex gap-2 mb-6">
        <input
          type="text"
          placeholder="Search AI news (e.g. OpenAI, LLMs, Nvidia)"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSearch()}
          className="flex-1 border rounded px-3 py-2"
        />
        <button
          onClick={handleSearch}
          className="px-4 py-2 bg-black text-white rounded"
        >
          Search
        </button>
      </div>

      <h2 className="text-xl font-semibold mb-4">📰 Latest AI News</h2>

      {loading && <p>Loading news...</p>}

      <div className="space-y-4">
        {news.map((item) => (
          <div
            key={item.id}
            className="border rounded p-4 flex justify-between items-start hover:bg-gray-50"
          >
            <div>
              <a
                href={item.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-lg font-semibold text-blue-600"
              >
                {item.title}
              </a>

              <div className="text-sm text-gray-600 mt-1">
                {item.source ?? "Unknown"} ·{" "}
                {new Date(item.published_at).toLocaleDateString()}
              </div>
            </div>
            
            <button
             onClick={() => addToFavorites(item)}
             className="ml-4 px-3 py-1 border rounded hover:bg-gray-100"
            >
            ⭐
            </button>

          </div>
        ))}
      </div>
    </main>
  );
}
