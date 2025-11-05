import type { Metadata } from 'next';
import SourcesList from './SourcesList';

export const metadata: Metadata = {
  title: 'Sources | EZ Manual Simplifier',
};

export default function SourcesPage() {
  return (
    <section>
      <h1>参照ソース一覧</h1>
      <p>
        簡易化ガイドの根拠となる公開情報をまとめています。ZIP 展開後や GitHub Pages
        で閲覧しても同じ JSON を参照できるよう、すべて <code>/data/</code> 配下に配置した
        静的ファイルから読み込んでいます。
      </p>
      <SourcesList />
    </section>
  );
}
