from google_play_scraper import Sort, reviews
import pandas as pd
import numpy as np

# 1. Konfigurasi Scraping
app_id = 'com.spotify.music' 
lang = 'id'
country = 'id'

print(f"Memulai scraping ulasan untuk {app_id}...")

# 2. Proses Ambil Data (Target 11.000 agar aman di atas 10k setelah cleaning)
result, continuation_token = reviews(
    app_id,
    lang=lang,
    country=country,
    sort=Sort.NEWEST,
    count=11000
)

df = pd.DataFrame(result)

# 3. Seleksi Kolom yang Dibutuhkan
# Kita ambil 'content' untuk teks dan 'score' untuk pelabelan
df = df[['content', 'score']]

# 4. Pelabelan Otomatis (Memenuhi Kriteria 2 & Saran: 3 Kelas)
# Skor 1-2: Negatif, Skor 3: Netral, Skor 4-5: Positif
def labeling(score):
    if score <= 2:
        return 'negatif'
    elif score == 3:
        return 'netral'
    else:
        return 'positif'

df['label'] = df['score'].apply(labeling)

# 5. Cek Distribusi Label
print("\nDistribusi Label:")
print(df['label'].value_counts())

# 6. Simpan ke CSV
df.to_csv('dataset_spotify_sentimen.csv', index=False)

print(f"\nSelesai! Berhasil mendapatkan {len(df)} baris data.")
print("File tersimpan: dataset_spotify_sentimen.csv")