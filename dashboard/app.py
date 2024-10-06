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

# Menampilkan histogram penyewaan sepeda
st.subheader("Histogram of Bike Rentals")
plt.figure(figsize=(10, 6))
plt.hist(df['cnt_x'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Total Bike Rentals (cnt_x)')
plt.ylabel('Frequency')
plt.title('Histogram of Bike Rentals per Day')
st.pyplot(plt)

# Menampilkan box plot penyewaan sepeda per musim
st.subheader("Box Plot of Bike Rentals per Season")
plt.figure(figsize=(10, 6))
sns.boxplot(x='season_x', y='cnt_x', data=df, palette='Set3')
plt.xlabel('Season (season_x)')
plt.ylabel('Total Bike Rentals (cnt_x)')
plt.title('Box Plot of Bike Rentals per Season')
st.pyplot(plt)

# Dampak cuaca pada penyewaan sepeda (visualisasi distribusi)
st.subheader("Impact of Weather on Bike Rentals")
plt.figure(figsize=(8, 6))
sns.boxplot(x='weathersit_x', y='cnt_x', data=df)
plt.xlabel('Weather Situation (weathersit_x)')
plt.ylabel('Total Bike Rentals (cnt_x)')
plt.title('Distribution of Bike Rentals by Weather Situation')
st.pyplot(plt)

# Analisis Cluster
st.subheader("Clustering Analysis of Bike Rentals")
features = ['temp_x', 'hum_x', 'windspeed_x', 'cnt_x']
X = df[features]

# Standarisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Membuat model KMeans
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X_scaled)

df['cluster'] = kmeans.labels_

# Visualisasi cluster
plt.figure(figsize=(10, 6))
plt.scatter(df['temp_x'], df['cnt_x'], c=df['cluster'], cmap='viridis')
plt.xlabel('Temperature (temp_x)')
plt.ylabel('Total Bike Rentals (cnt_x)')
plt.title('Clustering Results based on Temperature and Bike Rentals')
st.pyplot(plt)

# Run the Streamlit app
if _name_ == '_main_':
    st.write("Dashboard is ready!")
