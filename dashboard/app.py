import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load datasets
df = pd.read_csv('dashboard/main_data.csv')


# Convert 'dteday' to datetime
df1['dteday'] = pd.to_datetime(df1['dteday'])
df2['dteday'] = pd.to_datetime(df2['dteday'])

# Judul Dashboard 
st.title("Bike Rental Analysis Dashboard")

# Menampilkan data informasi
if st.checkbox('Show Data Information'):
    st.subheader('Day Dataset Information')
    st.write(df1.info())
    st.subheader('Hour Dataset Information')
    st.write(df2.info())

# Menampilkan statistik dasar
if st.checkbox('Show Descriptive Statistics'):
    st.subheader('Descriptive Statistics for Day Dataset')
    st.write(df1.describe())
    st.subheader('Descriptive Statistics for Hour Dataset')
    st.write(df2.describe())

# Menampilkan nilai yang hilang
if st.checkbox('Show Missing Values'):
    st.subheader('Missing Values in Day Dataset')
    st.write(df1.isnull().sum())
    st.subheader('Missing Values in Hour Dataset')
    st.write(df2.isnull().sum())

# Menampilkan grafik penyewaan sepeda per hari
if st.checkbox('Show Histogram of Bike Rentals per Day'):
    plt.figure(figsize=(10, 6))
    plt.hist(df1['cnt'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Total Bike Rentals')
    plt.ylabel('Frequency')
    plt.title('Histogram of Bike Rentals per Day')
    st.pyplot(plt)

# Menampilkan diagram penyewaan sepeda per musim
if st.checkbox('Show Box Plot of Bike Rentals per Season'):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=df1, palette='Set3')
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    plt.title('Box Plot of Bike Rentals per Season')
    st.pyplot(plt)

# Analisis dampak liburan pada penyewaan sepeda
if st.checkbox('Show Impact of Holiday on Bike Rentals'):
    holiday_rental = df1.groupby('holiday')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    plt.bar(holiday_rental.index, holiday_rental.values)
    plt.xlabel('Holiday (0: No, 1: Yes)')
    plt.ylabel('Average Bike Rentals')
    plt.title('Impact of Holiday on Bike Rentals')
    st.pyplot(plt)

# Dampak cuaca pada penyewaan sepeda
if st.checkbox('Show Impact of Weather on Bike Rentals'):
    weather_rental = df1.groupby('weathersit')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    plt.bar(weather_rental.index, weather_rental.values)
    plt.xlabel('Weather Situation (1: Clear, 2: Mist, 3: Light Snow/Rain, 4: Heavy Rain/Snow)')
    plt.ylabel('Average Bike Rentals')
    plt.title('Impact of Weather on Bike Rentals')
    st.pyplot(plt)

    # Diagram untuk situasi cuaca
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='weathersit', y='cnt', data=df1)
    plt.xlabel('Weather Situation')
    plt.ylabel('Total Bike Rentals')
    plt.title('Distribution of Bike Rentals by Weather Situation')
    st.pyplot(plt)

# Analisis Cluster
if st.checkbox('Show Clustering Analysis'):
    features = ['temp', 'hum', 'windspeed', 'cnt']
    X = df2[features]

    # Standar pada data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create KMeans model
    n_clusters = 3
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)
    
    df2['cluster'] = kmeans.labels_

    # Show cluster summary
    st.subheader('Cluster Summary')
    cluster_summary = df2.groupby('cluster')[features].mean()
    st.write(cluster_summary)

    # Visualisasi pada  clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(df2['temp'], df2['cnt'], c=df2['cluster'], cmap='viridis')
    plt.xlabel('Temperature')
    plt.ylabel('Total Bike Rentals')
    plt.title('Clustering Results based on Temperature and Bike Rentals')
    st.pyplot(plt)

# Run the Streamlit app
if __name__ == '__main__':
    st.write("Dashboard is ready!")
