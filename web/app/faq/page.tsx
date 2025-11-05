import type { Metadata } from 'next';

const faqs = [
  {
    question: 'ZIP だけで確認できますか？',
    answer:
      'はい。site-out.zip を解凍後に index.html を開くだけで、外部リソースへアクセスせず 5 ページの遷移を再現できます。'
  },
  {
    question: 'GitHub Pages への反映はどうなりますか？',
    answer:
      'feat/ui-phase1-next-export ブランチへの push または workflow_dispatch によって GitHub Actions が next export を実行し、gh-pages ブランチへ公開します。'
  },
  {
    question: 'データの更新手順は？',
    answer:
      'web/public/data 以下の JSON を編集し、ビルドを実行するだけで反映されます。末尾スラッシュのルーティングは自動的に維持されます。'
  }
];

export const metadata: Metadata = {
  title: 'FAQ | EZ Manual Simplifier',
};

export default function FaqPage() {
  return (
    <section>
      <h1>FAQ</h1>
      <p>UI Phase 1 のレビュー時によく寄せられる質問をまとめました。</p>
      <div className="details-group">
        {faqs.map((faq) => (
          <details key={faq.question}>
            <summary>{faq.question}</summary>
            <p>{faq.answer}</p>
          </details>
        ))}
      </div>
    </section>
  );
}
