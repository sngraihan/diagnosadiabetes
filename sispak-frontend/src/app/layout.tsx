import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

import Link from "next/link";

export const metadata: Metadata = {
  title: "SISPAK Diabetes",
  description: "Sistem Pakar Diagnosis Diabetes menggunakan Certainty Factor",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <nav className="bg-white border-b border-slate-200 sticky top-0 z-50">
          <div className="max-w-4xl mx-auto px-4 md:px-8 py-4 flex justify-between items-center">
            <Link href="/" className="font-bold text-xl text-blue-600 tracking-tight flex items-center gap-2">
              <span className="bg-blue-600 text-white rounded-lg w-8 h-8 flex items-center justify-center font-black">
                S
              </span>
              PakDiag
            </Link>
            <div className="flex gap-6 text-sm font-medium text-slate-600">
              <Link href="/" className="hover:text-blue-600 transition-colors">Beranda Prediksi</Link>
              <Link href="/tentang" className="hover:text-blue-600 transition-colors">Info & Edukasi</Link>
            </div>
          </div>
        </nav>
        {children}
      </body>
    </html>
  );
}
