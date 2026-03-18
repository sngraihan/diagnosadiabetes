from flask import Flask, request, jsonify
from flask_cors import CORS
from inference import run_inference

app = Flask(__name__)
# Aktifkan CORS agar frontend (Next.js) bisa me-request API ini dari origin/port yang berbeda
CORS(app)

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Menangkap data JSON yang dikirimkan oleh frontend
        data = request.json
        
        # Ekstrak data
        gdp_val = data.get('gdp', 0)
        gds_val = data.get('gds', 0)
        preg_val = data.get('preg', False)
        
        # Ekstrak dictionary gejala yang dikirim
        gejala_vals = data.get('gejala', {})

        # Panggil fungsi inference dari inference.py
        result = run_inference(gdp_val, gds_val, preg_val, gejala_vals)
        
        # Urutkan hasil dari CF yang tertinggi ke terendah
        sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)
        
        # Ambil diagnosis akhir (yang terbesar)
        if sorted_result:
            diagnosis_akhir = sorted_result[0][0]
            nilai_cf = sorted_result[0][1]
        else:
            diagnosis_akhir = "Tidak diketahui"
            nilai_cf = 0.0

        # Kembalikan response dalam bentuk JSON
        response = {
            "status": "success",
            "diagnosis_akhir": diagnosis_akhir,
            "nilai_cf": nilai_cf,
            "detail_hasil": dict(sorted_result)
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

if __name__ == '__main__':
    # Jalankan server API Flask di port 5000
    app.run(port=5000)
