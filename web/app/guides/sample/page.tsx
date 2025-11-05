import type { Metadata } from 'next';
import GuideTabs from './GuideTabs';

export const metadata: Metadata = {
  title: 'Sample Guide | EZ Manual Simplifier',
};

export default function SampleGuidePage() {
  return (
    <section>
      <h1>サンプルガイド</h1>
      <p>
        原文と簡易版の差分を素早く比較できるよう、タブ切り替えと対応表を用意しました。
        ZIP をローカル展開した場合でも <code>/data/guide-sample.json</code> を参照して同じ
        挙動を再現します。
      </p>
      <GuideTabs />
    </section>
  );
}
