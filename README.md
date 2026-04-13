# Sistem Prediksi Program Studi UNU Yogyakarta

Aplikasi web berbasis Machine Learning yang membantu calon mahasiswa menemukan program studi yang paling sesuai dengan profil akademik dan minat mereka di Universitas Nahdlatul Ulama Yogyakarta.

## Fitur Utama

- Design profesional dengan UNU Gold Theme (#BF8C16)
- Prediksi menggunakan algoritma Random Forest
- Penjelasan personal hasil rekomendasi
- Visualisasi interaktif tingkat kesesuaian
- Dark/Light mode
- Responsive untuk mobile dan desktop

## Tech Stack

- Frontend: Streamlit
- Backend: Python 
- Machine Learning: scikit-learn
- Data Processing: pandas, numpy

## Instalasi

Clone repository ini:
```bash
git clone https://github.com/ulililzam/siprodi.git
cd siprodi
```

Buat virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Train model (jika belum ada):
```bash
python train_model.py
```

Jalankan aplikasi:
```bash
streamlit run app.py
```

Buka browser di `http://localhost:8501`

## Cara Pakai

1. Masukkan nilai akademik kamu (Matematika, Bahasa Inggris, Agama, Fisika, Kimia, Biologi, Ekonomi)
2. Pilih tingkat minat di 4 bidang (Teknik, Kesehatan, Bisnis, Pendidikan)
3. Tentukan kemampuan hafalan (Ya/Tidak)
4. Klik "Prediksi Program Studi"
5. Lihat rekomendasi dan penjelasannya

## Program Studi Tersedia

1. S1 Informatika
2. S1 Teknik Elektro
3. S1 Farmasi
4. S1 Akuntansi
5. S1 Manajemen
6. S1 PGSD
7. S1 Pendidikan Bahasa Inggris
8. S1 Agribisnis
9. S1 Teknologi Hasil Pertanian
10. S1 Studi Islam Interdisipliner

## Deployment ke Streamlit Cloud

1. Push code ke GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Login dengan GitHub
4. Pilih repository ini
5. Deploy

Pastikan file `requirements.txt` lengkap dan model sudah ter-push ke repository.

## Model Info

- Dataset: 1000 sampel
- Features: 12 (7 nilai + 4 minat + 1 hafalan)
- Algorithm: Random Forest Classifier
- Accuracy: sekitar 85%

## Lisensi

MIT License - Bebas digunakan untuk pembelajaran dan pengembangan.

Dikembangkan untuk Universitas Nahdlatul Ulama Yogyakarta.
