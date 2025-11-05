import './globals.css';
import type { Metadata } from 'next';
import Link from 'next/link';
import { ReactNode } from 'react';

const navLinks = [
  { href: '/', label: 'Home' },
  { href: '/sources/', label: 'Sources' },
  { href: '/guides/', label: 'Guides' },
  { href: '/guides/sample/', label: 'Sample Guide' },
  { href: '/faq/', label: 'FAQ' },
];

export const metadata: Metadata = {
  title: 'EZ Manual Simplifier',
  description: 'UI phase-one prototype for validating static manual navigation on iPhone.',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="ja">
      <body>
        <header className="site-header">
          <div className="frame">
            <div className="branding">EZ Manual Simplifier</div>
            <nav aria-label="主要ナビゲーション">
              <ul>
                {navLinks.map((link) => (
                  <li key={link.href}>
                    <Link href={link.href}>{link.label}</Link>
                  </li>
                ))}
              </ul>
            </nav>
          </div>
        </header>
        <main className="frame content">{children}</main>
        <footer className="site-footer">
          <div className="frame">
            <small>© {new Date().getFullYear()} EZ Manual Simplifier</small>
          </div>
        </footer>
      </body>
    </html>
  );
}
