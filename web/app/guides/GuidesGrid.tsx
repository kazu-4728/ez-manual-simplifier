'use client';

import Link from 'next/link';
import { useEffect, useState } from 'react';

type Guide = {
  slug: string;
  title: string;
  sourceIds: string[];
  readingTimeMin: number;
  tags: string[];
};

export default function GuidesGrid() {
  const [guides, setGuides] = useState<Guide[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;
    fetch('/data/guides.json')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Failed to read guides: ${response.status}`);
        }
        return response.json() as Promise<Guide[]>;
      })
      .then((data) => {
        if (active) {
          setGuides(data);
        }
      })
      .catch(() => {
        if (active) {
          setError('ガイド情報を取得できませんでした。ZIP 展開場所を確認してください。');
        }
      });

    return () => {
      active = false;
    };
  }, []);

  if (error) {
    return <p>{error}</p>;
  }

  if (!guides.length) {
    return <p>読み込み中...</p>;
  }

  return (
    <div className="card-grid">
      {guides.map((guide) => (
        <article className="card" key={guide.slug}>
          <h3>{guide.title}</h3>
          <p>参照ソース: {guide.sourceIds.join(', ')}</p>
          <p>想定読了時間: 約 {guide.readingTimeMin} 分</p>
          <ul className="badge-row">
            {guide.tags.map((tag) => (
              <li key={tag} className="badge">
                {tag}
              </li>
            ))}
          </ul>
          <div style={{ marginTop: '1rem' }}>
            <Link href={`/guides/${guide.slug}/`}>詳細を見る →</Link>
          </div>
        </article>
      ))}
    </div>
  );
}
