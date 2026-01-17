"""
Aplikasi Prediksi Program Studi UNU Yogyakarta
UI Professional dengan UNU Gold Theme
"""

import streamlit as st
import pandas as pd
import pickle
import numpy as np

# ==================== KONFIGURASI HALAMAN ====================
st.set_page_config(
    page_title="Prediksi Prodi UNU Jogja",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== THEME STATE ====================
# Initialize theme in session state
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# ==================== CSS STYLING (UNU Gold Theme with Dark/Light Mode) ====================
def get_theme_css(theme='light'):
    """Generate CSS based on current theme"""
    
    # Theme colors
    if theme == 'dark':
        colors = {
            'main_bg': '#09090b',
            'card_bg': '#18181b',
            'card_text': '#fafafa',
            'section_header': '#fafafa',
            'label_text': '#d4d4d8',
            'input_bg': '#27272a',
            'input_border': '#3f3f46',
            'radio_bg': '#27272a',
            'radio_border': '#3f3f46',
            'radio_text': '#fafafa',
            'success_bg': '#422006',
            'success_text': '#fef3c7',
            'info_bg': '#27272a',
            'info_border': '#71717a',
            'conclusion_bg': 'linear-gradient(135deg, #422006 0%, #44403c 100%)',
            'conclusion_title': '#fbbf24',
            'conclusion_text': '#fef3c7',
            'metric_bg': '#27272a',
            'metric_border': '#3f3f46',
            'metric_label': '#a1a1aa',
            'metric_value': '#fafafa',
            'chart_bg': '#27272a',
            'chart_border': '#3f3f46',
            'title_border': '#3f3f46',
        }
    else:  # light theme
        colors = {
            'main_bg': '#09090b',
            'card_bg': 'white',
            'card_text': '#09090b',
            'section_header': '#18181b',
            'label_text': '#3f3f46',
            'input_bg': 'white',
            'input_border': '#e4e4e7',
            'radio_bg': '#fafafa',
            'radio_border': '#e4e4e7',
            'radio_text': '#000',
            'success_bg': '#fefce8',
            'success_text': '#713f12',
            'info_bg': '#f4f4f5',
            'info_border': '#71717a',
            'conclusion_bg': 'linear-gradient(135deg, #fefce8 0%, #fffbeb 100%)',
            'conclusion_title': '#713f12',
            'conclusion_text': '#854d0e',
            'metric_bg': '#fafafa',
            'metric_border': '#e4e4e7',
            'metric_label': '#52525b',
            'metric_value': '#18181b',
            'chart_bg': '#fafafa',
            'chart_border': '#e4e4e7',
            'title_border': '#f4f4f5',
        }
    
    return f"""
<style>
    /* Import Inter Font (UNU uses Inter) */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }}
    
    /* Main Container - Dark Background like UNU */
    .main {{
        background: {colors['main_bg']};
        padding: 2rem 1rem;
        transition: background 0.3s ease;
    }}
    
    /* Content Container */
    .block-container {{
        max-width: 1200px;
        padding: 2rem 1rem;
    }}
    
    /* Mobile Responsive */
    @media (max-width: 768px) {{
        .block-container {{
            padding: 1rem 0.5rem;
        }}
    }}
    
    /* Card Container - Theme Aware */
    .card-container {{
        background: {colors['card_bg']};
        border-radius: 8px;
        padding: 3rem 2.5rem;
        box-shadow: 0 4px 20px rgba(191, 140, 22, 0.15);
        margin: 1rem auto;
        border-top: 4px solid #BF8C16;
        transition: background 0.3s ease, box-shadow 0.3s ease;
    }}
    
    /* Mobile Responsive Card */
    @media (max-width: 768px) {{
        .card-container {{
            padding: 1.5rem 1rem;
            margin: 0.5rem auto;
        }}
    }}
    
    /* Header Title */
    .title-container {{
        text-align: center;
        margin-bottom: 2.5rem;
        padding-bottom: 2rem;
        border-bottom: 2px solid {colors['title_border']};
    }}
    
    /* Mobile Responsive Title */
    @media (max-width: 768px) {{
        .title-container {{
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
        }}
    }}
    
    .main-title {{
        font-size: 2.25rem;
        font-weight: 700;
        color: {colors['card_text']};
        margin: 0 0 0.75rem 0;
        letter-spacing: -0.5px;
    }}
    
    /* Mobile Responsive Title */
    @media (max-width: 768px) {{
        .main-title {{
            font-size: 1.5rem;
        }}
    }}
    
    .subtitle {{
        color: #71717a;
        font-size: 1rem;
        font-weight: 400;
        line-height: 1.5;
    }}
    
    /* Mobile Responsive Subtitle */
    @media (max-width: 768px) {{
        .subtitle {{
            font-size: 0.875rem;
        }}
    }}
    
    /* Theme Toggle Button */
    .theme-toggle {{
        position: fixed;
        top: 1rem;
        right: 1rem;
        z-index: 999;
        background: {colors['card_bg']};
        border: 2px solid #BF8C16;
        border-radius: 50px;
        padding: 0.5rem 1rem;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }}
    
    .theme-toggle:hover {{
        background: #BF8C16;
        transform: scale(1.05);
    }}
    
    /* Section Headers */
    .section-header {{
        font-size: 1.125rem;
        font-weight: 600;
        color: {colors['section_header']};
        margin: 2rem 0 1.25rem 0;
        padding-left: 1rem;
        border-left: 4px solid #BF8C16;
    }}
    
    /* Mobile Responsive Section Header */
    @media (max-width: 768px) {{
        .section-header {{
            font-size: 1rem;
            margin: 1.5rem 0 1rem 0;
        }}
    }}
    
    /* Input Labels - Clean Professional Style */
    .stSlider > label,
    .stSelectbox > label,
    .stRadio > label {{
        font-weight: 500 !important;
        color: {colors['label_text']} !important;
        font-size: 0.9rem !important;
    }}
    
    /* Mobile Responsive Labels */
    @media (max-width: 768px) {{
        .stSlider > label,
        .stSelectbox > label,
        .stRadio > label {{
            font-size: 0.85rem !important;
        }}
    }}
    
    /* Slider Styling - Gold Theme */
    .stSlider > div > div > div > div {{
        background: #BF8C16 !important;
    }}
    
    .stSlider > div > div > div {{
        background: #e4e4e7 !important;
    }}
    
    /* HIDE slider tick labels (0 and 100) */
    .stSlider [data-testid="stTickBar"] {{
        display: none !important;
    }}
    
    .stSlider > div[data-baseweb="slider"] > div:last-child {{
        display: none !important;
    }}
    
    /* Selectbox Styling */
    .stSelectbox > div > div {{
        background: {colors['input_bg']} !important;
        border-radius: 6px;
        border: 1.5px solid {colors['input_border']};
        transition: all 0.2s ease;
    }}
    
    .stSelectbox > div > div:hover,
    .stSelectbox > div > div:focus-within {{
        border-color: #BF8C16;
    }}
    
    /* Radio Button Styling - IMPROVED VISIBILITY */
    .stRadio > div {{
        background: {colors['radio_bg']};
        padding: 1rem;
        border-radius: 6px;
        border: 1px solid {colors['radio_border']};
    }}
    
    .stRadio > div > label {{
        color: {colors['radio_text']} !important;
    }}
    
    /* Radio button circle - NOT selected */
    .stRadio > div > label > div:first-child {{
        background-color: {colors['input_bg']} !important;
        border: 3px solid #a1a1aa !important;
        width: 24px !important;
        height: 24px !important;
    }}
    
    /* Radio button circle - SELECTED (Gold fill) */
    .stRadio > div > label > div:first-child:has(input:checked) {{
        background-color: #BF8C16 !important;
        border-color: #BF8C16 !important;
        box-shadow: 0 0 0 3px rgba(191, 140, 22, 0.2) !important;
    }}
    
    /* Inner dot when selected */
    .stRadio > div > label > div:first-child:has(input:checked)::after {{
        content: '';
        position: absolute;
        width: 10px;
        height: 10px;
        background: white;
        border-radius: 50%;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }}
    
    /* Button - Pill Shape with Gold Border (UNU Style) */
    .stButton > button {{
        width: 100%;
        background: #09090b;
        color: white;
        border: 2px solid #BF8C16;
        border-radius: 50px;
        padding: 0.875rem 2.5rem;
        font-size: 1rem;
        font-weight: 600;
        letter-spacing: 0.3px;
        transition: all 0.3s ease;
        margin-top: 2rem;
        text-transform: none;
    }}
    
    .stButton > button:hover {{
        background: #BF8C16;
        border-color: #BF8C16;
        transform: translateY(-1px);
        box-shadow: 0 8px 20px rgba(191, 140, 22, 0.3);
    }}
    
    /* Mobile Responsive Button */
    @media (max-width: 768px) {{
        .stButton > button {{
            padding: 0.75rem 2rem;
            font-size: 0.95rem;
        }}
    }}
    
    /* Success Box - Theme Aware */
    .element-container:has(.stAlert) {{
        margin: 2rem 0;
    }}
    
    div[data-testid="stMarkdownContainer"] > .stAlert {{
        background: {colors['success_bg']};
        border-left: 4px solid #BF8C16;
        border-radius: 6px;
        padding: 1.5rem;
        color: {colors['success_text']};
    }}
    
    /* Info Box */
    .stAlert[data-baseweb="notification"] {{
        background: {colors['info_bg']};
        border-left: 4px solid {colors['info_border']};
        border-radius: 6px;
        color: {colors['label_text']};
    }}
    
    /* Conclusion Box - Theme Aware */
    .conclusion-box {{
        background: {colors['conclusion_bg']};
        border: 2px solid #BF8C16;
        border-radius: 8px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(191, 140, 22, 0.1);
    }}
    
    /* Mobile Responsive Conclusion */
    @media (max-width: 768px) {{
        .conclusion-box {{
            padding: 1.5rem;
            margin: 1.5rem 0;
        }}
    }}
    
    .conclusion-title {{
        font-size: 1.25rem;
        font-weight: 700;
        color: {colors['conclusion_title']};
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    
    /* Mobile Responsive Conclusion Title */
    @media (max-width: 768px) {{
        .conclusion-title {{
            font-size: 1.1rem;
        }}
    }}
    
    .conclusion-text {{
        font-size: 1rem;
        line-height: 1.75;
        color: {colors['conclusion_text']};
    }}
    
    /* Mobile Responsive Conclusion Text */
    @media (max-width: 768px) {{
        .conclusion-text {{
            font-size: 0.9rem;
            line-height: 1.6;
        }}
    }}
    
    /* Metrics Styling - Theme Aware */
    .stMetric {{
        background: {colors['metric_bg']};
        padding: 1rem;
        border-radius: 6px;
        border: 1px solid {colors['metric_border']};
    }}
    
    .stMetric label {{
        color: {colors['metric_label']} !important;
        font-weight: 500 !important;
    }}
    
    .stMetric [data-testid="stMetricValue"] {{
        color: {colors['metric_value']} !important;
        font-size: 1.125rem !important;
    }}
    
    /* Mobile Responsive Metrics */
    @media (max-width: 768px) {{
        .stMetric {{
            padding: 0.75rem;
        }}
        
        .stMetric [data-testid="stMetricValue"] {{
            font-size: 1rem !important;
        }}
    }}
    
    /* Remove Streamlit Branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Smooth Animations */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    .card-container {{
        animation: fadeIn 0.5s ease-out;
    }}
    
    /* Chart Styling - Theme Aware */
    .stBarChart {{
        background: {colors['chart_bg']};
        padding: 1.5rem;
        border-radius: 6px;
        border: 1px solid {colors['chart_border']};
    }}
    
    /* Mobile Responsive Chart */
    @media (max-width: 768px) {{
        .stBarChart {{
            padding: 1rem;
        }}
    }}
    
    /* Column Responsive */
    @media (max-width: 768px) {{
        .row-widget.stHorizontal {{
            flex-direction: column !important;
        }}
        
        .row-widget.stHorizontal > div {{
            width: 100% !important;
        }}
    }}
</style>
"""

# Apply theme CSS
st.markdown(get_theme_css(st.session_state.theme), unsafe_allow_html=True)

# ==================== LOAD MODEL ====================
@st.cache_resource
def load_model():
    """Load trained model dari file pickle"""
    try:
        with open('model_unu_v2.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model tidak ditemukan! Silakan jalankan 'train_model.py' terlebih dahulu.")
        st.stop()

model = load_model()

# ==================== CONCLUSION GENERATOR ====================
def generate_conclusion(input_data, predicted_prodi, confidence):
    """
    Generate intelligent conclusion explaining why the student fits the program
    based on their academic scores and interests
    """
    # Extract values
    scores = {
        'Matematika': input_data['mtk'].values[0],
        'Bahasa Inggris': input_data['inggris'].values[0],
        'Pendidikan Agama': input_data['agama'].values[0],
        'Fisika': input_data['fisika'].values[0],
        'Kimia': input_data['kimia'].values[0],
        'Biologi': input_data['biologi'].values[0],
        'Ekonomi': input_data['ekonomi'].values[0]
    }
    
    interests = {
        'Teknik': input_data['minat_teknik'].values[0],
        'Kesehatan': input_data['minat_kesehatan'].values[0],
        'Bisnis': input_data['minat_bisnis'].values[0],
        'Pendidikan': input_data['minat_pendidikan'].values[0]
    }
    
    hafalan = input_data['hafalan'].values[0]
    
    # Find top 3 academic scores
    top_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Find top 2 interests
    top_interests = sorted(interests.items(), key=lambda x: x[1], reverse=True)[:2]
    
    # Generate conclusion based on predicted program
    conclusion_parts = []
    
    # Introduction - more casual tone
    conclusion_parts.append(f"Setelah menganalisis profil akademik dan minat kamu, sistem merekomendasikan *{predicted_prodi}* sebagai pilihan yang paling sesuai dengan karakteristik kamu.")
    
    # Academic strengths
    academic_strengths = []
    for subject, score in top_scores:
        if score >= 85:
            academic_strengths.append(f"{subject} ({score})")
    
    if academic_strengths:
        conclusion_parts.append(f"\n\n**Keunggulan Akademik:** Kamu punya prestasi yang bagus banget di {', '.join(academic_strengths)}, dan ini jadi modal kuat buat sukses di program studi ini.")
    
    # Interest alignment
    strong_interests = [name for name, level in top_interests if level >= 4]
    if strong_interests:
        conclusion_parts.append(f"\n\n**Kesesuaian Minat:** Minat kamu yang tinggi di bidang {' dan '.join(strong_interests)} cocok banget dengan apa yang bakal kamu pelajari dan peluang karir ke depannya.")
    
    # Special considerations
    if hafalan == 1 and "Islam" in predicted_prodi:
        conclusion_parts.append(f"\n\n**Kemampuan Khusus:** Kemampuan menghafal kamu yang bagus bakal jadi nilai plus dan sangat membantu dalam proses belajar di program studi ini.")
    
    # Program-specific insights
    program_insights = {
        'S1 Informatika': 'Program ini cocok bagi mereka dengan kemampuan logika dan matematika yang kuat serta passion di bidang teknologi.',
        'S1 Teknik Elektro': 'Program ini ideal untuk individu dengan kemampuan fisika dan matematika yang solid serta minat tinggi di bidang teknik.',
        'S1 Farmasi': 'Program ini sesuai untuk mereka yang unggul dalam kimia dan biologi dengan minat kuat di bidang kesehatan.',
        'S1 Akuntansi': 'Program ini tepat bagi mereka dengan kemampuan matematika yang baik dan minat di bidang bisnis dan keuangan.',
        'S1 Manajemen': 'Program ini cocok untuk individu dengan kemampuan ekonomi yang solid dan minat tinggi dalam bisnis.',
        'S1 PGSD': 'Program ini ideal bagi mereka dengan kemampuan akademik yang seimbang dan passion kuat di bidang pendidikan.',
        'S1 Pendidikan Bahasa Inggris': 'Program ini sesuai untuk mereka yang unggul dalam bahasa Inggris dengan minat tinggi di bidang pendidikan.',
        'S1 Agribisnis': 'Program ini tepat bagi mereka dengan kemampuan biologi dan ekonomi yang baik serta minat di bidang pertanian dan bisnis.',
        'S1 Teknologi Hasil Pertanian': 'Program ini cocok untuk individu dengan kemampuan kimia dan biologi yang solid serta minat di bidang teknologi pangan.',
        'S1 Studi Islam Interdisipliner': 'Program ini ideal bagi mereka dengan nilai pendidikan agama yang tinggi dan kemampuan menghafal yang baik.'
    }
    
    if predicted_prodi in program_insights:
        conclusion_parts.append(f"\n\n**Tentang Program:** {program_insights[predicted_prodi]}")
    
    # Confidence interpretation - more casual
    if confidence >= 70:
        conclusion_parts.append(f"\n\n**Tingkat Kesesuaian:** Dengan tingkat keyakinan {confidence:.1f}%, profil kamu sangat cocok dengan program studi ini. Boleh banget jadi pilihan utama!")
    elif confidence >= 50:
        conclusion_parts.append(f"\n\n**Tingkat Kesesuaian:** Dengan tingkat keyakinan {confidence:.1f}%, kamu punya potensi yang bagus untuk berkembang di program studi ini.")
    else:
        conclusion_parts.append(f"\n\n**Rekomendasi:** Ini adalah pilihan terbaik berdasarkan profil kamu, tapi ada baiknya kamu juga pertimbangkan opsi program studi lain dengan probabilitas tinggi supaya keputusannya lebih mantap.")
    
    return ' '.join(conclusion_parts)

# ==================== HEADER ====================
st.markdown("""
<div class="card-container">
    <div class="title-container">
        <h1 class="main-title">Sistem Prediksi Program Studi</h1>
        <p class="subtitle">Universitas Nahdlatul Ulama Yogyakarta<br>Machine Learning Recommendation System</p>
    </div>
""", unsafe_allow_html=True)

# ==================== THEME TOGGLE ====================
col_theme1, col_theme2, col_theme3 = st.columns([4, 1, 1])
with col_theme3:
    theme_icon = "🌙" if st.session_state.theme == 'light' else "☀️"
    theme_label = "Dark" if st.session_state.theme == 'light' else "Light"
    
    if st.button(f"{theme_icon} {theme_label}", key="theme_toggle", use_container_width=True):
        # Toggle theme
        st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
        st.rerun()

# ==================== FORM INPUT ====================
st.markdown('<p class="section-header">Data Nilai Akademik</p>', unsafe_allow_html=True)

# Baris 1: Nilai MTK, Inggris, Agama
col1, col2, col3 = st.columns(3)
with col1:
    mtk = st.slider("Matematika", 0, 100, 75, help="Nilai mata pelajaran Matematika")
with col2:
    inggris = st.slider("Bahasa Inggris", 0, 100, 75, help="Nilai mata pelajaran Bahasa Inggris")
with col3:
    agama = st.slider("Pendidikan Agama", 0, 100, 75, help="Nilai mata pelajaran Pendidikan Agama")

# Baris 2: Nilai Fisika, Kimia, Biologi, Ekonomi
col4, col5, col6, col7 = st.columns(4)
with col4:
    fisika = st.slider("Fisika", 0, 100, 70, help="Nilai mata pelajaran Fisika")
with col5:
    kimia = st.slider("Kimia", 0, 100, 70, help="Nilai mata pelajaran Kimia")
with col6:
    biologi = st.slider("Biologi", 0, 100, 70, help="Nilai mata pelajaran Biologi")
with col7:
    ekonomi = st.slider("Ekonomi", 0, 100, 70, help="Nilai mata pelajaran Ekonomi")

st.markdown('<p class="section-header">Minat dan Ketertarikan</p>', unsafe_allow_html=True)

# Baris 3: Minat (Selectbox dengan skala 1-5)
col8, col9, col10, col11 = st.columns(4)
with col8:
    minat_teknik = st.selectbox(
        "Minat Teknik",
        options=[1, 2, 3, 4, 5],
        index=2,
        help="1=Sangat Rendah, 5=Sangat Tinggi"
    )
with col9:
    minat_kesehatan = st.selectbox(
        "Minat Kesehatan",
        options=[1, 2, 3, 4, 5],
        index=2,
        help="1=Sangat Rendah, 5=Sangat Tinggi"
    )
with col10:
    minat_bisnis = st.selectbox(
        "Minat Bisnis",
        options=[1, 2, 3, 4, 5],
        index=2,
        help="1=Sangat Rendah, 5=Sangat Tinggi"
    )
with col11:
    minat_pendidikan = st.selectbox(
        "Minat Pendidikan",
        options=[1, 2, 3, 4, 5],
        index=2,
        help="1=Sangat Rendah, 5=Sangat Tinggi"
    )

st.markdown('<p class="section-header">Kemampuan Hafalan</p>', unsafe_allow_html=True)

# Hafalan (Radio Button)
hafalan_str = st.radio(
    "Apakah Anda memiliki kemampuan menghafal yang baik?",
    options=["Tidak", "Ya"],
    horizontal=True,
    help="Kemampuan menghafal Al-Qur'an atau teks keagamaan lainnya"
)
hafalan = 1 if hafalan_str == "Ya" else 0

# ==================== TOMBOL PREDIKSI ====================
if st.button("Prediksi Program Studi", use_container_width=True):
    # Buat DataFrame dengan urutan kolom SAMA PERSIS dengan train_model.py
    input_data = pd.DataFrame({
        'mtk': [mtk],
        'inggris': [inggris],
        'agama': [agama],
        'fisika': [fisika],
        'kimia': [kimia],
        'biologi': [biologi],
        'ekonomi': [ekonomi],
        'minat_teknik': [minat_teknik],
        'minat_kesehatan': [minat_kesehatan],
        'minat_bisnis': [minat_bisnis],
        'minat_pendidikan': [minat_pendidikan],
        'hafalan': [hafalan]
    })
    
    # Prediksi
    prediksi = model.predict(input_data)[0]
    probabilitas = model.predict_proba(input_data)[0]
    
    # Dapatkan semua kelas dan urutkan berdasarkan probabilitas
    kelas = model.classes_
    prob_df = pd.DataFrame({
        'Program Studi': kelas,
        'Probabilitas': probabilitas * 100
    }).sort_values('Probabilitas', ascending=False)
    
    # Ambil top 1 (hasil prediksi)
    confidence = prob_df.iloc[0]['Probabilitas']
    
    # ==================== HASIL PREDIKSI ====================
    st.markdown("---")
    st.markdown('<p class="section-header">Hasil Prediksi</p>', unsafe_allow_html=True)
    
    # Success box dengan hasil
    st.success(f"""
    **Program Studi yang Direkomendasikan:**
    
    # {prediksi}
    
    **Tingkat Keyakinan Sistem:** {confidence:.2f}%
    """)
    
    # ==================== KESIMPULAN CERDAS ====================
    conclusion = generate_conclusion(input_data, prediksi, confidence)
    
    st.markdown(f"""
    <div class="conclusion-box">
        <div class="conclusion-title">Kesimpulan dan Analisis</div>
        <div class="conclusion-text">{conclusion}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # ==================== GRAFIK PROBABILITAS ====================
    st.markdown('<p class="section-header">Tingkat Kesesuaian Semua Program Studi</p>', unsafe_allow_html=True)
    
    # Info box
    st.info("Grafik di bawah menunjukkan tingkat kesesuaian kamu dengan setiap program studi berdasarkan analisis sistem.")
    
    # Tampilkan bar chart
    st.bar_chart(
        prob_df.set_index('Program Studi')['Probabilitas'],
        height=400
    )
    
    # Tampilkan tabel detail
    with st.expander("Lihat Detail Probabilitas Semua Program Studi"):
        # Format tabel
        prob_df['Probabilitas'] = prob_df['Probabilitas'].apply(lambda x: f"{x:.2f}%")
        prob_df.index = range(1, len(prob_df) + 1)
        st.dataframe(prob_df, use_container_width=True)
    
    # Rekomendasi tambahan
    st.markdown('<p class="section-header">Rekomendasi Alternatif</p>', unsafe_allow_html=True)
    
    top_3 = prob_df.head(3)
    cols = st.columns(3)
    
    rank_labels = ["Pilihan Pertama", "Pilihan Kedua", "Pilihan Ketiga"]
    
    for idx, (_, row) in enumerate(top_3.iterrows()):
        with cols[idx]:
            st.metric(
                label=rank_labels[idx],
                value=row['Program Studi'],
                delta=row['Probabilitas']
            )

# ==================== FOOTER ====================
st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e4e4e7; color: #71717a; font-size: 0.875rem;">
        <p style="margin: 0.5rem 0;">Developed for Universitas Nahdlatul Ulama Yogyakarta</p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem; color: #a1a1aa;">Powered by Machine Learning and Streamlit</p>
    </div>
</div>
""", unsafe_allow_html=True)
