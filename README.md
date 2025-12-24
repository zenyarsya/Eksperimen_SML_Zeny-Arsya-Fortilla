# Eksperimen Preprocessing Data Retail Marketing

Repository ini berisi seluruh rangkaian eksperimen awal, eksplorasi data, dan pemrosesan data (preprocessing) untuk proyek segmentasi pelanggan retail.

## 📂 Struktur File Eksperimen
- **`Eksperimen_Zeny_Arsya_Fortilla.ipynb`**: Notebook utama yang berisi langkah-langkah eksplorasi data (EDA), pembersihan data, dan transformasi fitur.
- **`OnlineRetail.zip`**: Dataset mentah (raw data) transaksi retail yang digunakan dalam eksperimen ini.
- **`OnlineRetail_preprocessed.zip`**: Dataset hasil akhir yang telah dibersihkan dan siap digunakan untuk proses pelatihan model.
- **`automate_Zeny-Arsya-Fortilla.py`**: Script otomatisasi untuk menjalankan alur preprocessing secara programmatik.

## 🛠️ Alur Kerja Eksperimen
1. **Pembersihan Data**: Menangani nilai yang hilang (missing values) dan menghapus entri transaksi yang tidak valid (misalnya, pembatalan pesanan).
2. **Transformasi Fitur**: Melakukan agregasi data transaksi per pelanggan untuk mendapatkan metrik kunci seperti RFM (Recency, Frequency, Monetary).
3. **Otomatisasi**: Mengonversi langkah-langkah notebook ke dalam script Python (`.py`) agar dapat dijalankan ulang dengan mudah dalam alur kerja MLOps.

## 🔗 Hubungan dengan Proyek Utama
Hasil dari eksperimen di repository ini merupakan fondasi utama bagi repository model saya:
👉 **[Repository Utama MLOps](https://github.com/zenyarsya/Submission-MLOps-Zeny-Arsya-Fortilla)**
