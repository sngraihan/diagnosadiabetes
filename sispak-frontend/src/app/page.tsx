import Link from 'next/link';

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center font-sans p-4 relative overflow-hidden">
      {/* Background decorations - Standard Tailwind */}
      <div className="absolute top-0 -left-10 w-72 h-72 bg-blue-200 rounded-full mix-blend-multiply blur-3xl opacity-50 animate-pulse transition-all duration-1000"></div>
      <div className="absolute top-0 -right-10 w-72 h-72 bg-emerald-200 rounded-full mix-blend-multiply blur-3xl opacity-50 animate-pulse transition-all duration-[3000ms]"></div>
      <div className="absolute -bottom-8 left-20 w-72 h-72 bg-indigo-200 rounded-full mix-blend-multiply blur-3xl opacity-50 animate-pulse transition-all duration-[4000ms]"></div>

      <div className="max-w-3xl w-full bg-white/80 backdrop-blur-2xl rounded-3xl shadow-2xl p-8 md:p-14 text-center border border-white/50 relative z-10 transition-all hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.1)]">
        

        <h1 className="text-4xl md:text-5xl lg:text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-700 to-indigo-600 mb-6 tracking-tight">
          Cek Risiko Diabetes Anda
        </h1>
        
        <p className="text-lg md:text-xl text-slate-600 mb-10 leading-relaxed max-w-2xl mx-auto">
          Sistem Pakar cerdas berbasis <span className="font-semibold text-blue-600">Certainty Factor</span> yang membantu Anda mendeteksi potensi penyakit Diabetes Melitus Tipe 1, Tipe 2, dan Gestasional.
        </p>

        <div className="flex flex-col sm:flex-row justify-center gap-4">
          <Link href="/prediksi" 
            className="group relative px-8 py-4 bg-blue-600 text-white font-bold rounded-2xl shadow-xl shadow-blue-500/30 hover:shadow-blue-500/50 hover:-translate-y-1 transition-all duration-300 flex items-center justify-center overflow-hidden">
            <span className="relative z-10 flex items-center gap-2">
              Mulai Prediksi Sekarang
              <svg className="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 7l5 5m0 0l-5 5m5-5H6"></path></svg>
            </span>
            <div className="absolute inset-0 bg-indigo-600 translate-y-full group-hover:translate-y-0 transition-transform duration-300 rounded-2xl"></div>
          </Link>
          
          <Link href="/tentang"
            className="px-8 py-4 bg-slate-100 text-slate-700 font-bold rounded-2xl border border-slate-200 hover:bg-slate-200 hover:text-slate-900 transition-all duration-200 flex items-center justify-center shadow-sm">
            Pelajari Lebih Lanjut
          </Link>
        </div>
        
      </div>
    </div>
  );
}
