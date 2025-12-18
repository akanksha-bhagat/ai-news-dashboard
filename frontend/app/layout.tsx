import './globals.css';
import Link from 'next/link';

export const metadata = {
  title: 'AI News Dashboard',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        {/* Top Navigation */}
        <header className="border-b mb-6">
          <div className="max-w-4xl mx-auto p-4 flex justify-between items-center">
            <h1 className="text-2xl font-bold">🧠 AI News Dashboard</h1>

            <Link
              href="/favorites"
              className="text-yellow-600 font-semibold hover:underline"
            >
              ⭐ View Favorites
            </Link>
          </div>
        </header>

        {children}
      </body>
    </html>
  );
}
