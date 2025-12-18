"use client";

import { useEffect, useState } from "react";

type Favorite = {
  id: number;
  title: string;
  url: string;
  source: string;
};

export default function FavoritesPage() {
  const [favorites, setFavorites] = useState<Favorite[]>([]);
  const API = process.env.NEXT_PUBLIC_API_URL;

  useEffect(() => {
    fetch(`${API}/favorites`)
      .then((res) => res.json())
      .then(setFavorites);
  }, []);

  const broadcast = async (id: number, platform: string) => {
    await fetch(`${API}/favorites/${id}/broadcast/${platform}`, {
      method: "POST",
    });
    alert(`Broadcasted via ${platform}`);
  };

  return (
    <main className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">⭐ Favorites</h1>

      {favorites.map((f) => (
        <div key={f.id} className="border p-4 mb-4 rounded">
          <a
            href={f.url}
            target="_blank"
            className="text-lg font-semibold text-blue-600"
          >
            {f.title}
          </a>

          <p className="text-sm text-gray-600">Source: {f.source}</p>

          <div className="mt-2 space-x-2">
            <button onClick={() => broadcast(f.id, "email")}>Email</button>
            <button onClick={() => broadcast(f.id, "linkedin")}>LinkedIn</button>
            <button onClick={() => broadcast(f.id, "whatsapp")}>WhatsApp</button>
            <button onClick={() => broadcast(f.id, "newsletter")}>Newsletter</button>
          </div>
        </div>
      ))}
    </main>
  );
}
