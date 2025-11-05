'use client';

import { useEffect, useState } from 'react';

type Source = {
  id: string;
  title: string;
  url: string;
  lastUpdatedJst: string;
  highlights: string[];
};

export default function SourcesList() {
  const [sources, setSources] = useState<Source[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;
    fetch('/data/sources.json')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Failed to read sources: ${response.status}`);
        }
        return response.json() as Promise<Source[]>;
      })
      .then((data) => {
        if (active) {
          setSources(data);
        }
      })
      .catch(() => {
        if (active) {
          setError('データを取得できませんでした。ZIP 展開後のパスを確認してください。');
        }
      });

    return () => {
      active = false;
    };
  }, []);

  if (error) {
    return <p>{error}</p>;
  }

  if (!sources.length) {
    return <p>読み込み中...</p>;
  }

  return (
    <ul className="data-list">
      {sources.map((source) => (
        <li key={source.id}>
          <strong>{source.title}</strong>
          <p>
            <a href={source.url} target="_blank" rel="noreferrer">
              {source.url}
            </a>
          </p>
          <p>最終更新（JST）: {source.lastUpdatedJst}</p>
          <ul className="badge-row">
            {source.highlights.map((highlight) => (
              <li key={highlight} className="badge">
                {highlight}
              </li>
            ))}
          </ul>
        </li>
      ))}
    </ul>
  );
}
