import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('dashboard/main_data.csv')

# Data Exploration for main_data.csv
def explore_data(df):
    print("Lima baris teratas dari data main_data.csv:")
    print(df.head())
    print("\nInformasi umum dari data main_data.csv:")
    print(df.info())
    print("\nStatistik deskriptif dari data main_data.csv:")
    print(df.describe())
    print("\nJumlah nilai yang hilang (missing values) dalam data main_data.csv:")
    print(df.isnull().sum())
    print("\nJumlah duplikat pada data main_data.csv:")
    print(df.duplicated().sum())

    # Grouping analysis
    print("\nTotal Bike Rentals per Season:")
    print(df.groupby('season')['cnt'].sum())
    print("\nTotal Bike Rentals per Year:")
    print(df.groupby('yr')['cnt'].sum())
    print("\nTotal Bike Rentals per Month:")
    print(df.groupby('mnth')['cnt'].sum())
    print("\nTotal Bike Rentals per Weekday:")
    print(df.groupby('weekday')['cnt'].sum())
    print("\nTotal Bike Rentals per Weather Situation:")
    print(df.groupby('weathersit')['cnt'].sum())

    # Correlation matrix
    correlation_matrix = df.corr()
    print("\nCorrelation Matrix for main_data.csv:")
    print(correlation_matrix)

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix for Main Data')
    plt.show()

    # Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['cnt'], bins=20)
    plt.xlabel('Total Bike Rentals')
    plt.ylabel('Frequency')
    plt.title('Histogram of Bike Rentals')
    plt.show()

    # Box plot per season
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=df)
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    plt.title('Box Plot of Bike Rentals per Season')
    plt.show()

# Analyze the impact of holidays on bike rentals
def analyze_holiday_impact(df):
    holiday_rental = df.groupby('holiday')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    plt.bar(holiday_rental.index, holiday_rental.values)
    plt.xlabel('Holiday (0: No, 1: Yes)')
    plt.ylabel('Average Bike Rentals')
    plt.title('Impact of Holiday on Bike Rentals')
    plt.show()

# Analyze the impact of weather on bike rentals
def analyze_weather_impact(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weekday', y='cnt', hue='weathersit', data=df)
    plt.xlabel('Weekday')
    plt.ylabel('Total Bike Rentals')
    plt.title('Impact of Weather and Weekday on Bike Rentals')
    plt.show()

    # Scatter plots
    for feature in ['temp', 'hum', 'windspeed']:
        plt.figure(figsize=(10, 6))
        plt.scatter(df[feature], df['cnt'])
        plt.xlabel(feature.capitalize())
        plt.ylabel('Total Bike Rentals')
        plt.title(f'Impact of {feature.capitalize()} on Bike Rentals')
        plt.show()

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
    print(cluster_summary)

    # Visualization of clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(df['temp'], df['cnt'], c=df['cluster'], cmap='viridis')
    plt.xlabel('Temperature')
    plt.ylabel('Total Bike Rentals')
    plt.title('Clustering Results based on Temperature and Bike Rentals')
    plt.show()

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
