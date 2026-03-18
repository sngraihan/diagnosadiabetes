import React from "react";

export const metadata = {
  title: "Tim Pengembang | SISPAK Diabetes",
};

const TEAM_MEMBERS = [
  { name: "Amala Ratri Nugraheni", npm: "2317051007", role: "Anggota Tim" },
  { name: "Raihan Andi Saungnaga", npm: "2317051058", role: "Anggota Tim" },
  { name: "Achmad Ghalib Hafizh", npm: "2317051023", role: "Anggota Tim" },
  { name: "Zidan Ahmad At-Thoriq", npm: "2317051050", role: "Anggota Tim" },
];

export default function TimPage() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 p-4 md:p-8 font-sans">
      <div className="max-w-4xl mx-auto space-y-12 py-8">
        
        <header className="text-center space-y-4">
          <div className="inline-block bg-blue-100 text-blue-700 font-bold px-4 py-1.5 rounded-full text-sm mb-2 shadow-sm border border-blue-200">
            Kredit Pembuatan Prototipe
          </div>
          <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight text-slate-800">
            Tim Pengembang
          </h1>
          <p className="text-lg text-slate-500 max-w-2xl mx-auto">
            Aplikasi Sistem Pakar Diagnosis Diabetes Melitus (Metode Certainty Factor) ini dikembangkan sebagai bentuk nyata implementasi keilmuan oleh:
          </p>
        </header>

        <main>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {TEAM_MEMBERS.map((member, index) => (
              <div 
                key={index} 
                className="bg-white rounded-2xl p-6 shadow-xl shadow-slate-200/40 border border-slate-100 hover:border-blue-300 hover:shadow-blue-100/50 transition-all group flex items-start gap-4"
              >
                {/* Avatar Placeholder */}
                <div className="w-16 h-16 rounded-full bg-gradient-to-br from-blue-100 to-indigo-100 flex items-center justify-center text-blue-600 font-bold text-2xl shadow-inner border-2 border-white flex-shrink-0 group-hover:scale-110 transition-transform">
                  {member.name.charAt(0)}
                </div>
                
                {/* Info Text */}
                <div className="space-y-1">
                  <h2 className="text-xl font-bold text-slate-800 group-hover:text-blue-600 transition-colors">
                    {member.name}
                  </h2>
                  <div className="flex flex-col gap-1">
                    <span className="text-sm font-medium text-slate-500 bg-slate-100 px-2.5 py-0.5 rounded-md w-max">
                      NPM: {member.npm}
                    </span>
                    <span className="text-sm text-slate-400 font-medium">
                      Mahasiswa Ilmu Komputer
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </main>

        <footer className="text-center pt-10 text-slate-400 text-sm font-medium">
          <p>© {new Date().getFullYear()} Universitas Lampung. All rights reserved.</p>
        </footer>

      </div>
    </div>
  );
}
