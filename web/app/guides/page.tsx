import type { Metadata } from 'next';
import GuidesGrid from './GuidesGrid';

export const metadata: Metadata = {
  title: 'Guides | EZ Manual Simplifier',
};

export default function GuidesPage() {
  return (
    <section>
      <h1>簡易ガイド一覧</h1>
      <p>
        現段階ではサンプルガイドを 1 本だけ提供していますが、カード UI とデータ構造は
        拡張を想定しており、JSON にエントリを追加するだけで新しいガイドを露出できます。
      </p>
      <GuidesGrid />
    </section>
  );
}
