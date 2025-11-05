const navigationChecklist = [
  'ホームから各ページへ遷移しても末尾スラッシュのURLが維持されることを確認。',
  'Sourcesでリンクとハイライトが読み込まれるまで待ち、内容を確認。',
  'Guidesのカードからサンプルガイドにアクセスし、タブ切り替えを試す。'
];

const recentUpdates = [
  {
    label: '静的JSONを元にしたガイド／ソース表示を実装し、オフライン確認を容易化。',
    date: '2024-04-30'
  },
  {
    label: 'ガイド詳細に原文と簡易版のタブ切り替えを追加。',
    date: '2024-04-28'
  },
  {
    label: 'FAQをdetails要素で再構成し、iPhoneでの折り畳みを改善。',
    date: '2024-04-26'
  }
];

export default function HomePage() {
  return (
    <section>
      <h1>UI Phase 1 の目的</h1>
      <p>
        iPhone Safari 上で 5 ページ構成の静的 UI を検証し、ガイド閲覧の体験を
        確認するためのプロトタイプです。Next.js 14 の <code>next export</code> を用いて
        完全静的化し、GitHub Pages と Artifacts の両方で配布できる構成になっています。
      </p>
      <div className="card-grid">
        <div className="card">
          <h3>使い方</h3>
          <ol>
            <li>Draft PR の Checks から <strong>site-out.zip</strong> を取得し解凍。</li>
            <li>または GitHub Pages の公開 URL を iPhone Safari で開く。</li>
            <li>ヘッダーのナビゲーションから 5 ページすべてを巡回。</li>
          </ol>
        </div>
        <div className="card">
          <h3>確認チェック</h3>
          <ul>
            {navigationChecklist.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
        <div className="card">
          <h3>開発メモ</h3>
          <p>
            外部リソースに依存しないため、ZIP を iPhone のファイル App で展開した
            場合でも同じ UI を確認できます。
          </p>
        </div>
      </div>
      <div className="updates">
        <h2>最近の更新</h2>
        <ul className="data-list">
          {recentUpdates.map((update) => (
            <li key={update.label}>
              <strong>{update.date}</strong>
              <p>{update.label}</p>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
