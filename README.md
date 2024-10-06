# Analisis-Bike-Sharing
Deskripsi Proyek 
Repositori ini berisi proyek analisis data yang berfokus pada eksplorasi data penyewaan sepeda. Hal ini bertujuan untuk mengungkap wawasan mengenai faktor-faktor yang memengaruhi penyewaan sepeda, seperti kondisi cuaca, hari libur, musim, hari biasa dan lainnya. Selain itu, repositori ini juga mencakup analisis pengelompokan untuk mengelompokkan data berdasarkan fitur-fitur utama.

# Struktur Direktori
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt

# Dataset
hour.csv : Pada data set ini berisikan informasi tentang berapa jam penyewa menyewa sepeda.
day.csv : Pada data set ini berisikan informasi mengenai suhu, kelembapan pada saat menyewa sepeda setiap harinya.

# Visualisasi
**Matriks Korelasi**
 Pada visualisasi ini menunjukan adanya fitur fitur yang berbeda didataset. Visualisasi ini membantu memahami variable yang mana berkorelasi kuat dengan penyewaan sepeda.

**Grafik Penyewaan Sepeda**
  Grafik ini memvisualisasikan distribusi total penyewaan sepeda yang dimana untuk menunjukan frekuensi jumlah penyewaan yang berbeda.

**Katagori Penyewaan Sepeda per Musim**
  Yang dimana mengkatagorikan penyewaan sepeda berdasarkan setiap musim, sehingga lebih memudahkan untuk bisa membandingkan setiap tahunnya.

**Analisis Pengelompokan**
 Untuk mengelompokkan data ke dalam beberapa cluster yang diterapkan pada fitur-fitur yang dipilih seperti suhu,kelembapan,kecepatan angin, dan jumlah penyewaan sepeda. Hasil dari divisualisasikan menunjukkan tingkat suhu dan penyewaan sepeda yang berbeda membentuk cluster.

# Penggunaan
1. # Setup Lingkungan di Google Colab

   Pastikan untuk install library yang memang diperlukan lalu jalankan kode berikut ini:
   !pip install -r requirements.txt
   
2. # Menajalankan Dashboard

   Ketika library sudah terinstall, lalu jalankan aplikasi streamlit dengan perintah berikut:
   !streamlit run dashboard/app.py & npx localtunnel --port 8501

3. # Link Dashboard
   Untuk Link Dasboard bisa di akses melalui url : https://achgik7ygfgngbkan6n5yz.streamlit.app/
