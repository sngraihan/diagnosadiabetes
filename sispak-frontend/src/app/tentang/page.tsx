import React from "react";

export const metadata = {
  title: "Tentang Sistem | SISPAK Diabetes",
};

export default function TentangPage() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 p-4 md:p-8 font-sans">
      <div className="max-w-4xl mx-auto space-y-8">
        
        <header className="text-center space-y-2 mb-10">
          <h1 className="text-4xl font-extrabold tracking-tight text-blue-600">
            Info & Edukasi Sistem
          </h1>
          <p className="text-lg text-slate-500">
            Penjelasan Metode & Basis Pengetahuan
          </p>
        </header>

        <main className="space-y-8">
          
          <section className="bg-white p-6 md:p-8 rounded-2xl shadow-xl shadow-slate-200/50 border border-slate-100">
            <h2 className="text-2xl font-bold mb-4 text-slate-700 flex items-center gap-2">
              <span className="text-3xl"></span> Metode Certainty Factor (CF)
            </h2>
            <div className="text-slate-600 space-y-4 leading-relaxed">
              <p>
                Aplikasi ini dibangun menggunakan metode komputasi murni dari <strong>Certainty Factor (Faktor Kepastian)</strong>. 
                Metode ini pertama kali dikembangkan di Universitas Stanford sebagai bentuk penalaran ekspert buatan yang menangani ketidakpastian.
              </p>
              <p>
                Cara kerjanya adalah dengan menggabungkan nilai kepastian kepakaran (<em>Measure of Belief</em> dan <em>Measure of Disbelief</em>) dengan nilai keyakinan dari pengguna saat memasukkan gejala. Semakin kuat indikasi gejala yang dialami, semakin tinggi persentase diagnosis akhirnya.
              </p>
            </div>
          </section>

          <section className="bg-gradient-to-br from-blue-600 to-indigo-700 p-6 md:p-8 rounded-2xl shadow-xl shadow-blue-200/50 text-white">
            <h2 className="text-2xl font-bold mb-4 flex items-center gap-2">
              <span className="text-3xl">🩺</span> Jenis Diabetes yang Dideteksi
            </h2>
            <ul className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
              <li className="bg-white/10 p-4 rounded-xl backdrop-blur-sm border border-white/20">
                <h3 className="font-bold text-lg mb-2 text-blue-100">Diabetes Tipe 1</h3>
                <p className="text-sm text-blue-100/80">
                  Kerusakan pada pankreas sehingga gagal memproduksi insulin. Sering terjadi pada usia muda.
                </p>
              </li>
              <li className="bg-white/10 p-4 rounded-xl backdrop-blur-sm border border-white/20">
                <h3 className="font-bold text-lg mb-2 text-blue-100">Diabetes Tipe 2</h3>
                <p className="text-sm text-blue-100/80">
                  Resistensi sel tubuh terhadap insulin. Sangat dipengaruhi oleh pola makan, gaya hidup, dan obesitas.
                </p>
              </li>
              <li className="bg-white/10 p-4 rounded-xl backdrop-blur-sm border border-white/20">
                <h3 className="font-bold text-lg mb-2 text-blue-100">Gestasional</h3>
                <p className="text-sm text-blue-100/80">
                  Terjadi khusus pada wanita yang sedang hamil akibat perubahan hormon, dan bisa hilang pasca persalinan.
                </p>
              </li>
            </ul>
          </section>

          <section className="bg-white p-6 md:p-8 rounded-2xl shadow-xl shadow-slate-200/50 border border-slate-100 mb-8">
            <h2 className="text-2xl font-bold mb-4 text-slate-700">Peringatan Medis</h2>
            <div className="bg-amber-50 text-amber-800 p-4 rounded-xl border border-amber-200 text-sm font-medium">
              Sistem pakar ini hanyalah prototipe simulasi berbasis kecerdasan buatan terbatas. Hasil perhitungan probabilitas tidak dapat menggantikan diagnosis medis resmi dari dokter spesialis atau fasilitas kesehatan profesional.
            </div>
          </section>

        </main>

      </div>
    </div>
  );
}
