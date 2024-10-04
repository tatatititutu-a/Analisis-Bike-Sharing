import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import streamlit as st

# Load dataset
df = pd.read_csv('dashboard/main_data.csv')

# data eksplor main_data
def explore_data(df):
    # Visualization - Correlation matrix
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix for Main Data')
    st.pyplot(plt)

    # grafik penyewaan sepeda
    plt.figure(figsize=(10, 6))
    plt.hist(df['cnt'], bins=20)
    plt.xlabel('Total Bike Rentals')
    plt.ylabel('Frequency')
    plt.title('Histogram of Bike Rentals')
    st.pyplot(plt)

    # grafik per season
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=df)
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    plt.title('Box Plot of Bike Rentals per Season')
    st.pyplot(plt)

# analisis penyewaan sepeda pada hari libur 
def analyze_holiday_impact(df):
    holiday_rental = df.groupby('holiday')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    plt.bar(holiday_rental.index, holiday_rental.values)
    plt.xlabel('Holiday (0: No, 1: Yes)')
    plt.ylabel('Average Bike Rentals')
    plt.title('Impact of Holiday on Bike Rentals')
    st.pyplot(plt)

# analisa dampak dari cuaca
def analyze_weather_impact(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weekday', y='cnt', hue='weathersit', data=df)
    plt.xlabel('Weekday')
    plt.ylabel('Total Bike Rentals')
    plt.title('Impact of Weather and Weekday on Bike Rentals')
    st.pyplot(plt)

    # grafik pada suhu, kelembapan dan angin
    for feature in ['temp', 'hum', 'windspeed']:
        plt.figure(figsize=(10, 6))
        plt.scatter(df[feature], df['cnt'])
        plt.xlabel(feature.capitalize())
        plt.ylabel('Total Bike Rentals')
        plt.title(f'Impact of {feature.capitalize()} on Bike Rentals')
        st.pyplot(plt)

# clustering analisis
def clustering_analysis(df):
    features = ['temp', 'hum', 'windspeed', 'cnt']
    X = df[features]
    
    # standar pada data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # KMeans clustering
    n_clusters = 3
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)
    
    df['cluster'] = kmeans.labels_

    # visualisasi pada  clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(df['temp'], df['cnt'], c=df['cluster'], cmap='viridis')
    plt.xlabel('Temperature')
    plt.ylabel('Total Bike Rentals')
    plt.title('Clustering Results based on Temperature and Bike Rentals')
    st.pyplot(plt)

# running program
if __name__ == "__main__":
    # mengkonfersi data pada kolom date
    df['dteday'] = pd.to_datetime(df['dteday'])

    # menampilkan visualisasi
    st.title('Bike Rental Data Visualization')

    explore_data(df)
    analyze_holiday_impact(df)
    analyze_weather_impact(df)
    clustering_analysis(df)
