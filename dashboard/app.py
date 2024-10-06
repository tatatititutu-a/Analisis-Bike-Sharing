import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('dashboard/main_data.csv')

# Convert 'dteday' to datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Judul Dashboard 
st.title("Bike Rental Analysis Dashboard")

# Visualization - Correlation matrix
st.subheader("Correlation Matrix")
correlation_matrix = df.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for Main Data')
st.pyplot(plt)

# Menampilkan histogram penyewaan sepeda
st.subheader("Histogram of Bike Rentals")
plt.figure(figsize=(10, 6))
plt.hist(df['cnt'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Total Bike Rentals (cnt)')
plt.ylabel('Frequency')
plt.title('Histogram of Bike Rentals per Day')
st.pyplot(plt)

# Menampilkan box plot penyewaan sepeda per musim
st.subheader("Box Plot of Bike Rentals per Season")
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=df, palette='Set3')
plt.xlabel('Season')
plt.ylabel('Total Bike Rentals (cnt)')
plt.title('Box Plot of Bike Rentals per Season')
st.pyplot(plt)

# Dampak cuaca pada penyewaan sepeda (visualisasi distribusi)
st.subheader("Impact of Weather on Bike Rentals")
plt.figure(figsize=(8, 6))
sns.boxplot(x='weathersit', y='cnt', data=df)
plt.xlabel('Weather Situation')
plt.ylabel('Total Bike Rentals (cnt)')
plt.title('Distribution of Bike Rentals by Weather Situation')
st.pyplot(plt)

# Analisis Cluster
st.subheader("Clustering Analysis of Bike Rentals")
features = ['temp', 'hum', 'windspeed', 'cnt']  # Ganti 'cnt_x' ke 'cnt'
X = df[features]

# Standarisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Membuat kolom baru 'season_weather' yang menggabungkan musim dan cuaca
df1['season_weather'] = df1['season'].astype(str) + '_' + df1['weathersit'].astype(str)

# Menampilkan jumlah penyewaan sepeda untuk setiap kelompok 'season_weather'
season_weather_rental = df1.groupby('season_weather')['cnt'].mean().reset_index()

# Menyimpan hasil ke dalam file CSV
season_weather_rental.to_csv('dashboard/main_data.csv', index=False)

# Visualisasi jumlah penyewaan sepeda untuk setiap kelompok
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
season_weather_rental.plot(kind='bar', x='season_weather', y='cnt', legend=False)
plt.xlabel('Season and Weather')
plt.ylabel('Average Bike Rentals')
plt.title('Average Bike Rentals by Season and Weather')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  # Menyesuaikan layout agar tidak terpotong
plt.savefig('average_bike_rentals_by_season_and_weather.png')  # Menyimpan gambar
plt.show()

# Menentukan kelompok berdasarkan jumlah penyewaan sepeda
high_rental = season_weather_rental[season_weather_rental['cnt'] > 5000]['season_weather'].tolist()
medium_rental = season_weather_rental[(season_weather_rental['cnt'] >= 2000) & (season_weather_rental['cnt'] <= 5000)]['season_weather'].tolist()
low_rental = season_weather_rental[season_weather_rental['cnt'] < 2000]['season_weather'].tolist()

print("Kelompok Penyewaan Tinggi:", high_rental)
print("Kelompok Penyewaan Sedang:", medium_rental)
print("Kelompok Penyewaan Rendah:", low_rental)
