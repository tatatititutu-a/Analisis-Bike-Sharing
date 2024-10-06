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

# Display the first few rows of the dataset
st.subheader("Main Data Preview")
st.write(main_data.head())

# Display statistics of the dataset
st.subheader("Statistics")
st.write(main_data.describe())

# Display missing values
st.subheader("Missing Values")
st.write(main_data.isnull().sum())

# Visualization - Correlation matrix
st.subheader("Correlation matrix")
correlation_matrix = df.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for Main Data')
st.pyplot(plt)

# Histogram of bike rentals
st.subheader("Histogram of Bike Rentals")
plt.figure(figsize=(10, 6))
plt.hist(main_data['cnt_day'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Total Bike Rentals')
plt.ylabel('Frequency')
plt.title('Histogram of Bike Rentals per Day')
st.pyplot(plt)

# Boxplot of bike rentals per season
st.subheader("Box Plot of Bike Rentals per Season")
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt_day', data=main_data, palette='Set3')
plt.xlabel('Season')
plt.ylabel('Total Bike Rentals')
plt.title('Box Plot of Bike Rentals per Season')
st.pyplot(plt)
