import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'AI Kubernetes Agent',
  description: 'An on-demand AI troubleshooting workflow for Kubernetes',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
