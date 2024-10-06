import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load datasets
df1 = pd.read_csv('day.csv')
df2 = pd.read_csv('hour.csv')

# Bagian Data Explor
st.title("Bike Rental Analysis Dashboard")

st.header("Data Overview")
if st.checkbox('Show first five rows of day.csv'):
    st.write(df1.head())
    
if st.checkbox('Show information of day.csv'):
    buffer = pd.io.formats.format.StringFormatter().to_string(df1.info())
    st.text(buffer)

if st.checkbox('Show descriptive statistics of day.csv'):
    st.write(df1.describe())
    
if st.checkbox('Show missing values in day.csv'):
    st.write(df1.isnull().sum())

if st.checkbox('Show first five rows of hour.csv'):
    st.write(df2.head())
    
if st.checkbox('Show information of hour.csv'):
    buffer = pd.io.formats.format.StringFormatter().to_string(df2.info())
    st.text(buffer)

if st.checkbox('Show descriptive statistics of hour.csv'):
    st.write(df2.describe())

if st.checkbox('Show missing values in hour.csv'):
    st.write(df2.isnull().sum())

# Bagian visualisasi
st.header("Visualizations")

# Korelasi Matrix file day.csv
if st.checkbox('Show Correlation Matrix for Day Data'):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df1.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix for Day Data')
    st.pyplot()

# Grafik penyewaan sepeda file day
if st.checkbox('Show Histogram of Bike Rentals per Day'):
    plt.figure(figsize=(10, 6))
    plt.hist(df1['cnt'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Total Bike Rentals')
    plt.ylabel('Frequency')
    plt.title('Histogram of Bike Rentals per Day')
    st.pyplot()

# Grafik per season
if st.checkbox('Show Box Plot of Bike Rentals per Season'):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=df1, palette='Set3')
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    plt.title('Box Plot of Bike Rentals per Season')
    st.pyplot()

# Grafik penyewaan sepeda
if st.checkbox('Show Impact of Holiday on Bike Rentals'):
    holiday_rental = df1.groupby('holiday')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    plt.bar(holiday_rental.index, holiday_rental.values)
    plt.xlabel('Holiday (0: No, 1: Yes)')
    plt.ylabel('Average Bike Rentals')
    plt.title('Impact of Holiday on Bike Rentals')
    st.pyplot()

# Rata-rata Sewa Berdasarkan Cuaca
if st.checkbox('Show Impact of Weather on Bike Rentals'):
    weather_rental = df1.groupby('weathersit')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    plt.bar(weather_rental.index, weather_rental.values)
    plt.xlabel('Weather Situation (1: Clear, 2: Mist, 3: Light Snow/Rain, 4: Heavy Rain/Snow)')
    plt.ylabel('Average Bike Rentals')
    plt.title('Impact of Weather on Bike Rentals')
    st.pyplot()

# Distribusi Penyewaan Sepeda Berdasarkan Cuaca
if st.checkbox('Show Distribution of Bike Rentals by Weather Situation'):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='weathersit', y='cnt', data=df1)
    plt.xlabel('Weather Situation')
    plt.ylabel('Total Bike Rentals')
    plt.title('Distribution of Bike Rentals by Weather Situation')
    st.pyplot()

# Analisi bagian cluster
st.header("Clustering Analysis")
if st.checkbox('Show Clustering Results'):
    features = ['temp', 'hum', 'windspeed', 'cnt']
    X = df2[features]
    
    # Stadar pada data 
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # KMeans Clustering
    n_clusters = 3
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)
    
    # Tambahkan label cluster ke DataFrame
    df2['cluster'] = kmeans.labels_
    
    # Tampilan ringkasan klaster
    cluster_summary = df2.groupby('cluster')[features].mean()
    st.write("Cluster Summary:")
    st.write(cluster_summary)

    # Visualisasi hasil Cluster
    plt.figure(figsize=(10, 6))
    plt.scatter(df2['temp'], df2['cnt'], c=df2['cluster'], cmap='viridis')
    plt.xlabel('Temperature')
    plt.ylabel('Total Bike Rentals')
    plt.title('Clustering Results based on Temperature and Bike Rentals')
    st.pyplot()
