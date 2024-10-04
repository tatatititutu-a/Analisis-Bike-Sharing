import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import streamlit as st  # Impor Streamlit

# Load dataset
df = pd.read_csv('dashboard/main_data.csv')

# Data Exploration for main_data.csv
def explore_data(df):
    st.write("Lima baris teratas dari data main_data.csv:")
    st.write(df.head())
    st.write("\nInformasi umum dari data main_data.csv:")
    st.write(df.info())
    st.write("\nStatistik deskriptif dari data main_data.csv:")
    st.write(df.describe())
    st.write("\nJumlah nilai yang hilang (missing values) dalam data main_data.csv:")
    st.write(df.isnull().sum())
    st.write("\nJumlah duplikat pada data main_data.csv:")
    st.write(df.duplicated().sum())

    # Grouping analysis
    st.write("\nTotal Bike Rentals per Season:")
    st.write(df.groupby('season')['cnt'].sum())
    st.write("\nTotal Bike Rentals per Year:")
    st.write(df.groupby('yr')['cnt'].sum())
    st.write("\nTotal Bike Rentals per Month:")
    st.write(df.groupby('mnth')['cnt'].sum())
    st.write("\nTotal Bike Rentals per Weekday:")
    st.write(df.groupby('weekday')['cnt'].sum())
    st.write("\nTotal Bike Rentals per Weather Situation:")
    st.write(df.groupby('weathersit')['cnt'].sum())

    # Correlation matrix
    correlation_matrix = df.corr()
    st.write("\nCorrelation Matrix for main_data.csv:")
    st.write(correlation_matrix)

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix for Main Data')
    st.pyplot(plt)  # Ganti plt.show() dengan st.pyplot()

    # Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['cnt'], bins=20)
    plt.xlabel('Total Bike Rentals')
    plt.ylabel('Frequency')
    plt.title('Histogram of Bike Rentals')
    st.pyplot(plt)  # Ganti plt.show() dengan st.pyplot()

    # Box plot per season
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=df)
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    plt.title('Box Plot of Bike Rentals per Season')
    st.pyplot(plt)  # Ganti plt.show() dengan st.pyplot()

# Analyze the impact of holidays on bike rentals
def analyze_holiday_impact(df):
    holiday_rental = df.groupby('holiday')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    plt.bar(holiday_rental.index, holiday_rental.values)
    plt.xlabel('Holiday (0: No, 1: Yes)')
    plt.ylabel('Average Bike Rentals')
    plt.title('Impact of Holiday on Bike Rentals')
    st.pyplot(plt)  # Ganti plt.show() dengan st.pyplot()

# Analyze the impact of weather on bike rentals
def analyze_weather_impact(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weekday', y='cnt', hue='weathersit', data=df)
    plt.xlabel('Weekday')
    plt.ylabel('Total Bike Rentals')
    plt.title('Impact of Weather and Weekday on Bike Rentals')
    st.pyplot(plt)  # Ganti plt.show() dengan st.pyplot()

    # Scatter plots
    for feature in ['temp', 'hum', 'windspeed']:
        plt.figure(figsize=(10, 6))
        plt.scatter(df[feature], df['cnt'])
        plt.xlabel(feature.capitalize())
        plt.ylabel('Total Bike Rentals')
        plt.title(f'Impact of {feature.capitalize()} on Bike Rentals')
        st.pyplot(plt)  # Ganti plt.show() dengan st.pyplot()

# Clustering analysis
def clustering_analysis(df):
    features = ['temp', 'hum', 'windspeed', 'cnt']
    X = df[features]
    
    # Standardizing the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # KMeans clustering
    n_clusters = 3
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)
    
    df['cluster'] = kmeans.labels_
    
    # Summary of clusters
    cluster_summary = df.groupby('cluster')[features].mean()
    st.write(cluster_summary)

    # Visualization of clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(df['temp'], df['cnt'], c=df['cluster'], cmap='viridis')
    plt.xlabel('Temperature')
    plt.ylabel('Total Bike Rentals')
    plt.title('Clustering Results based on Temperature and Bike Rentals')
    st.pyplot(plt)  # Ganti plt.show() dengan st.pyplot()

# Main execution
if __name__ == "__main__":
    # Convert date column
    df['dteday'] = pd.to_datetime(df['dteday'])

    # Explore the dataset
    explore_data(df)

    # Analyze impacts
    analyze_holiday_impact(df)
    analyze_weather_impact(df)

    # Perform clustering analysis
    clustering_analysis(df)
