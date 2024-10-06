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

# Sidebar for selection
analysis_type = st.sidebar.selectbox(
    "Choose the analysis to display:",
    ("Overview", "Correlation Matrix", "Bike Rentals by Season", "Holiday Impact", "Weather Impact", "Season and Weather Analysis")
)

# Overview of datasets
if analysis_type == "Overview":
st.subheader("Overview of Day Dataset")
st.write(df1.head())
st.write(df1.describe())
st.subheader("Overview of Hour Dataset")
st.write(df2.head())
st.write(df2.describe())

# Correlation Matrix
elif analysis_type == "Correlation Matrix":
st.subheader("Correlation Matrix for Day Data")
correlation_matrix_day = df1.corr()
sns.heatmap(correlation_matrix_day, annot=True, cmap='coolwarm')
st.pyplot()
st.subheader("Correlation Matrix for Hour Data")
correlation_matrix_hour = df2.corr()
sns.heatmap(correlation_matrix_hour, annot=True, cmap='coolwarm')
st.pyplot()

# Bike Rentals by Season
elif analysis_type == "Bike Rentals by Season":
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=df1, palette='Set3')
plt.xlabel('Season')
plt.ylabel('Total Bike Rentals')
plt.title('Box Plot of Bike Rentals per Season')
st.pyplot()

# Impact of Holiday
elif analysis_type == "Holiday Impact":
holiday_rental = df1.groupby('holiday')['cnt'].mean()
plt.figure(figsize=(8, 6))
plt.bar(holiday_rental.index, holiday_rental.values)
plt.xlabel('Holiday (0: No, 1: Yes)')
plt.ylabel('Average Bike Rentals')
plt.title('Impact of Holiday on Bike Rentals')
st.pyplot()

# Impact of Weather
elif analysis_type == "Weather Impact":
weather_rental = df1.groupby('weathersit')['cnt'].mean()
plt.figure(figsize=(8, 6))
plt.bar(weather_rental.index, weather_rental.values)
plt.xlabel('Weather Situation (1: Clear, 2: Mist, 3: Light Snow/Rain, 4: Heavy Rain/Snow)')
plt.ylabel('Average Bike Rentals')
plt.title('Impact of Weather on Bike Rentals')
st.pyplot()

# Season and Weather Analysis
elif analysis_type == "Season and Weather Analysis":
df1['season_weather'] = df1['season'].astype(str) + '_' + df1['weathersit'].astype(str)
season_weather_rental = df1.groupby('season_weather')['cnt'].mean()
    
plt.figure(figsize=(12, 6))
season_weather_rental.plot(kind='bar')
plt.xlabel('Season and Weather')
plt.ylabel('Average Bike Rentals')
plt.title('Average Bike Rentals by Season and Weather')
plt.xticks(rotation=45, ha='right')
st.pyplot()

# Displaying the rental groups
st.subheader("Rental Groups")
high_rental = season_weather_rental[season_weather_rental > 5000].index.tolist()
medium_rental = season_weather_rental[(season_weather_rental >= 2000) & (season_weather_rental <= 5000)].index.tolist()
low_rental = season_weather_rental[season_weather_rental < 2000].index.tolist()

st.write("High Rental Groups:", high_rental)
st.write("Medium Rental Groups:", medium_rental)
st.write("Low Rental Groups:", low_rental)
