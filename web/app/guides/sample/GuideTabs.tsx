'use client';

import { useEffect, useMemo, useState } from 'react';

type GuideSection = {
  id: string;
  html: string;
};

type GuidePayload = {
  original: GuideSection[];
  simplified: GuideSection[];
  mapping: { origId: string; simpId: string }[];
};

type TabKey = 'simplified' | 'original';

const tabs: { key: TabKey; label: string }[] = [
  { key: 'simplified', label: '簡易版' },
  { key: 'original', label: '原文' }
];

export default function GuideTabs() {
  const [guide, setGuide] = useState<GuidePayload | null>(null);
  const [activeTab, setActiveTab] = useState<TabKey>('simplified');
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;
    fetch('/data/guide-sample.json')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Failed to read guide data: ${response.status}`);
        }
        return response.json() as Promise<GuidePayload>;
      })
      .then((data) => {
        if (active) {
          setGuide(data);
        }
      })
      .catch(() => {
        if (active) {
          setError('ガイドデータを取得できませんでした。ZIP 展開場所を確認してください。');
        }
      });

    return () => {
      active = false;
    };
  }, []);

  const mappingDescription = useMemo(() => {
    if (!guide) {
      return [] as string[];
    }
    return guide.mapping.map((pair) => `原文 ${pair.origId} → 簡易 ${pair.simpId}`);
  }, [guide]);

  if (error) {
    return <p>{error}</p>;
  }

  if (!guide) {
    return <p>読み込み中...</p>;
  }

  const sections = activeTab === 'simplified' ? guide.simplified : guide.original;

  return (
    <div>
      <div className="tab-list" role="tablist" aria-label="原文と簡易版の切り替え">
        {tabs.map((tab) => (
          <button
            key={tab.key}
            type="button"
            role="tab"
            aria-selected={activeTab === tab.key}
            aria-pressed={activeTab === tab.key}
            onClick={() => setActiveTab(tab.key)}
          >
            {tab.label}
          </button>
        ))}
      </div>
      <div className="tab-panel" role="tabpanel">
        {sections.map((section) => (
          <section key={section.id} dangerouslySetInnerHTML={{ __html: section.html }} />
        ))}
      </div>
      {mappingDescription.length > 0 && (
        <div className="mapping">
          <strong>対応表</strong>
          <ul>
            {mappingDescription.map((text) => (
              <li key={text}>{text}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
