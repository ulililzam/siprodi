# Sistem Prediksi Program Studi UNU Yogyakarta

<div align="center">

![UNU Yogyakarta](https://img.shields.io/badge/UNU-Yogyakarta-BF8C16?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

**Aplikasi rekomendasi program studi berbasis Machine Learning dengan UNU Gold Theme**

[Live Demo](https://siprodi.streamlit.app) • [Dokumentasi](#dokumentasi) • [Kontribusi](#kontribusi)

</div>

---

## 📋 Deskripsi

Sistem Prediksi Program Studi adalah aplikasi web berbasis Machine Learning yang membantu calon mahasiswa menemukan program studi yang paling sesuai dengan profil akademik dan minat mereka di Universitas Nahdlatul Ulama Yogyakarta.

### ✨ Fitur Utama

- 🎨 **UNU Gold Theme** - Design profesional dengan warna khas UNU (#BF8C16)
- 🤖 **Machine Learning** - Prediksi akurat menggunakan Random Forest
- 💡 **Kesimpulan Cerdas** - Penjelasan personal mengapa cocok dengan prodi tertentu
- 📊 **Visualisasi Interaktif** - Grafik probabilitas untuk semua program studi
- 📱 **Responsive Design** - Tampilan optimal di semua device

### 🎓 Program Studi yang Tersedia

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

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip

### Instalasi Lokal

1. Clone repository
```bash
git clone https://github.com/ulililzam/siprodi.git
cd siprodi
```

2. Buat virtual environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# atau
venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Train model (jika model belum ada)
```bash
python train_model.py
```

5. Jalankan aplikasi
```bash
streamlit run app.py
```

6. Buka browser di `http://localhost:8501`

---

## 📊 Cara Penggunaan

1. **Input Data Akademik**
   - Masukkan nilai mata pelajaran (0-100)
   - Matematika, Bahasa Inggris, Pendidikan Agama
   - Fisika, Kimia, Biologi, Ekonomi

2. **Pilih Minat**
   - Teknik (1-5)
   - Kesehatan (1-5)
   - Bisnis (1-5)
   - Pendidikan (1-5)

3. **Kemampuan Hafalan**
   - Pilih Ya/Tidak

4. **Lihat Hasil**
   - Rekomendasi program studi
   - Tingkat keyakinan sistem
   - Kesimpulan personal
   - Grafik probabilitas semua prodi
   - Top 3 pilihan alternatif

---

## 🛠️ Teknologi

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: scikit-learn (Random Forest Classifier)
- **Data Processing**: pandas, numpy
- **Styling**: Custom CSS (UNU Gold Theme)

---

## 📁 Struktur Project

```
siprodi/
├── app.py                    # Main Streamlit application
├── train_model.py            # Model training script
├── model_unu_v2.pkl         # Trained ML model
├── dataset_unu_1000csv.csv  # Training dataset
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # Documentation
```

---

## 🎨 Design System

### Color Palette

- **Primary Gold**: `#BF8C16` - Aksen utama (border, button, highlight)
- **Dark Background**: `#09090b` - Background gelap profesional
- **White**: `#ffffff` - Content cards
- **Grey Shades**: `#f4f4f5`, `#e4e4e7`, `#71717a` - UI elements

### Typography

- **Font**: Inter (Google Fonts)
- **Style**: Clean, professional, minimalist

---

## 🤖 Model Machine Learning

### Dataset
- **Total**: 1000 sampel
- **Features**: 12 (7 nilai akademik + 4 minat + 1 hafalan)
- **Target**: 10 program studi

### Algoritma
- **Random Forest Classifier**
- **Accuracy**: ~85%+

### Training
```bash
python train_model.py
```

---

## 🌐 Deployment (Streamlit Cloud)

### Langkah Deploy:

1. Push ke GitHub
2. Login ke [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository
4. Deploy!

### Environment
Pastikan `requirements.txt` berisi:
```
pandas>=1.5.0
scikit-learn>=1.2.0
streamlit>=1.28.0
numpy>=1.24.0
```

---

## 📝 Lisensi

MIT License - Bebas digunakan untuk pembelajaran dan pengembangan

---

## 👨‍💻 Developer

Dikembangkan untuk **Universitas Nahdlatul Ulama Yogyakarta**

---

## 🙏 Kontribusi

Kontribusi sangat diterima! Silakan:
1. Fork repository
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

<div align="center">

**Made with ❤️ for UNU Yogyakarta**

![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-FF4B4B?style=flat-square&logo=streamlit)
![Machine Learning](https://img.shields.io/badge/AI-Machine%20Learning-brightgreen?style=flat-square)

</div>
