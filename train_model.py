"""
Train Model untuk Prediksi Program Studi UNU Yogyakarta
Menggunakan RandomForestClassifier dengan akurasi tinggi
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

def main():
    print("="*60)
    print("SISTEM TRAINING MODEL PREDIKSI PRODI UNU YOGYAKARTA")
    print("="*60)
    
    # 1. Load Dataset
    print("\n[1] Loading dataset...")
    df = pd.read_csv('dataset_unu_1000.csv')
    print(f"✓ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"✓ Jumlah Program Studi: {df['prodi'].nunique()}")
    print(f"\nProgram Studi yang tersedia:")
    for idx, prodi in enumerate(df['prodi'].unique(), 1):
        print(f"   {idx}. {prodi}")
    
    # 2. Split Features dan Target
    print("\n[2] Memisahkan Features dan Target...")
    # Urutan kolom HARUS SAMA dengan yang di app.py
    feature_columns = [
        'mtk', 'inggris', 'agama', 'fisika', 'kimia', 'biologi', 'ekonomi',
        'minat_teknik', 'minat_kesehatan', 'minat_bisnis', 'minat_pendidikan',
        'hafalan'
    ]
    
    X = df[feature_columns]
    y = df['prodi']
    print(f"✓ Features shape: {X.shape}")
    print(f"✓ Target shape: {y.shape}")
    
    # 3. Split Data 80/20
    print("\n[3] Splitting data (80% training, 20% testing)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"✓ Training set: {X_train.shape[0]} samples")
    print(f"✓ Testing set: {X_test.shape[0]} samples")
    
    # 4. Train Model
    print("\n[4] Training RandomForestClassifier...")
    print("   Parameters: n_estimators=100, random_state=42")
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1,  # Gunakan semua CPU cores
        max_depth=20,  # Batasi kedalaman untuk menghindari overfitting
        min_samples_split=5
    )
    
    model.fit(X_train, y_train)
    print("✓ Training selesai!")
    
    # 5. Evaluasi Model
    print("\n[5] Evaluasi Model...")
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    train_accuracy = accuracy_score(y_train, y_pred_train)
    test_accuracy = accuracy_score(y_test, y_pred_test)
    
    print(f"\n{'='*60}")
    print(f"HASIL AKURASI MODEL:")
    print(f"{'='*60}")
    print(f"Training Accuracy : {train_accuracy*100:.2f}%")
    print(f"Testing Accuracy  : {test_accuracy*100:.2f}%")
    print(f"{'='*60}")
    
    # Feature Importance
    print("\n[6] Feature Importance (Top 5):")
    feature_importance = pd.DataFrame({
        'feature': feature_columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    for idx, row in feature_importance.head(5).iterrows():
        print(f"   {row['feature']:20s} : {row['importance']:.4f}")
    
    # 6. Save Model
    print("\n[7] Menyimpan model...")
    with open('model_unu_v2.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("✓ Model berhasil disimpan ke 'model_unu_v2.pkl'")
    
    # Detailed Classification Report
    print("\n[8] Classification Report (Test Set):")
    print("="*60)
    print(classification_report(y_test, y_pred_test, zero_division=0))
    
    print("\n" + "="*60)
    print("TRAINING SELESAI! Model siap digunakan untuk prediksi.")
    print("="*60)

if __name__ == "__main__":
    main()
