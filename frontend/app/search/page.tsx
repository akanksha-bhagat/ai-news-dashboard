"use client";

import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";

type SearchResult = {
  title: string;
  url: string;
  source: string;
  similarity: number;
};

export default function SearchPage() {
  const searchParams = useSearchParams();
  const query = searchParams.get("q");

  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);

  const API = process.env.NEXT_PUBLIC_API_URL;

  useEffect(() => {
    if (!query) return;

    setLoading(true);

    fetch(`${API}/search?q=${encodeURIComponent(query)}`)
      .then((res) => res.json())
      .then((data) => setResults(data))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, [query]);

  return (
    <main className="p-6 max-w-5xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">
        🔍 Search results for “{query}”
      </h1>

      {loading && <p>Searching...</p>}

      {!loading && results.length === 0 && (
        <p>No results found.</p>
      )}

      <div className="space-y-4">
        {results.map((item, idx) => (
          <div
            key={idx}
            className="border rounded p-4 hover:bg-gray-50"
          >
            <a
              href={item.url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-lg font-semibold text-blue-600"
            >
              {item.title}
            </a>

            <div className="text-sm text-gray-600 mt-1">
              {item.source} · Similarity: {item.similarity.toFixed(2)}
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
