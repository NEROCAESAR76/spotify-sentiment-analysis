# 🎧 Spotify Pulse: Deep Sentiment Analytics
> **Transforming raw user feedback into actionable product intelligence using Bi-Directional Deep Learning.**

![Python](https://img.shields.io/badge/Language-Python%203.9-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/Framework-TensorFlow%202.x-orange?style=for-the-badge&logo=tensorflow)
![Status](https://img.shields.io/badge/Accuracy-93.14%25-success?style=for-the-badge)
![Niche](https://img.shields.io/badge/Domain-NLP%20%7C%20Sentiment%20Analysis-blueviolet?style=for-the-badge)

---

## 🌊 Project Overview
Spotify Pulse bukan sekadar klasifikasi teks biasa. Ini adalah sebuah *pipeline* analitik yang dirancang untuk membedah emosi pengguna di balik ulasan aplikasi Spotify. Dengan memanfaatkan arsitektur **Bidirectional Long Short-Term Memory (Bi-LSTM)**, model ini mampu memahami konteks kalimat dari dua arah, menangkap nuansa sarkasme maupun keluhan teknis yang sering terlewatkan oleh model linear tradisional.

### 🧠 The Core Challenge
Bagaimana kita bisa mendapatkan akurasi **>92%** pada data ulasan yang penuh dengan bahasa *slang* Indonesia, singkatan "alay", dan ketidakseimbangan kelas (*imbalance data*)? Proyek ini menjawab tantangan tersebut dengan teknik *Global Max Pooling* dan *Masking* yang presisi.

---

## 🚀 Key Engineering Features
* **Deep Contextual Understanding**: Menggunakan Bi-LSTM untuk memproses urutan teks secara maju dan mundur.
* **Robust Preprocessing**: *Custom pipeline* untuk normalisasi bahasa gaul (Indonesian slang) dan pembersihan derau (*noise reduction*).
* **Anti-Amnesia Padding**: Implementasi `mask_zero=True` pada layer Embedding untuk memastikan model tidak kehilangan informasi pada kalimat pendek.
* **Imbalance Handling**: Optimasi distribusi bobot kelas untuk memastikan ulasan negatif (kritik) didengar sama jelasnya dengan ulasan positif.

---

## 🏗️ Technical Architecture
Model ini dibangun dengan struktur berlapis yang dioptimasi untuk kecepatan dan akurasi:
1.  **Input Layer**: Tokenized sequences (>10k samples).
2.  **Embedding Layer**: 128-dimensional vector space with Masking.
3.  **Core Engine**: Bidirectional LSTM (64 units) with Dropout 0.5.
4.  **Attention Mechanism**: Global MaxPooling1D untuk menangkap sinyal sentimen terkuat.
5.  **Output Layer**: Softmax activation untuk 3-class classification (Positif, Netral, Negatif).

---

## 📈 Performance Benchmarks
| Experiment | Architecture | Train Acc | Test Acc | Status |
| :--- | :--- | :---: | :---: | :---: |
| Baseline | Standard LSTM | 89.1% | 87.6% | ✅ Passed |
| Variant A | GRU Engine | 90.0% | 88.0% | ✅ Passed |
| **Production** | **Bi-LSTM Optimized** | **93.14%** | **92.45%** | 🏆 **Best** |

---

## 🛠️ Installation & Setup
```bash
# Clone the intelligence
git clone https://github.com/NEROCAESAR76/spotify-pulse.git

# Enter the directory
cd spotify-pulse

# Install dependencies
pip install -r requirements.txt
