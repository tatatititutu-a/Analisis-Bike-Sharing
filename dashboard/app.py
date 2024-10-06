import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
df1 = pd.read_csv('day.csv')
df2 = pd.read_csv('hour.csv')

# Title of the dashboard
st.title("Bike Rental Analysis Dashboard")

# Exploring day.csv
st.subheader("Exploring day.csv")
st.write(df1.head())
st.write(df1.describe())

# Visualizing correlation matrix for day.csv
st.subheader("Correlation Matrix for Day Data")
correlation_matrix_day = df1.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix_day, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for Day Data')
st.pyplot(plt)

# Visualizing bike rentals per day
st.subheader("Histogram of Bike Rentals per Day")
plt.figure(figsize=(10, 6))
plt.hist(df1['cnt'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Total Bike Rentals')
plt.ylabel('Frequency')
plt.title('Histogram of Bike Rentals per Day')
st.pyplot(plt)

# Analysis of bike rentals by season
st.subheader("Box Plot of Bike Rentals by Season")
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=df1, palette='Set3')
plt.xlabel('Season')
plt.ylabel('Total Bike Rentals')
plt.title('Box Plot of Bike Rentals by Season')
st.pyplot(plt)

# Impact of Holiday on Bike Rentals
st.subheader("Impact of Holiday on Bike Rentals")
holiday_rental = df1.groupby('holiday')['cnt'].mean()
plt.figure(figsize=(8, 6))
plt.bar(holiday_rental.index, holiday_rental.values)
plt.xlabel('Holiday (0: No, 1: Yes)')
plt.ylabel('Average Bike Rentals')
plt.title('Impact of Holiday on Bike Rentals')
st.pyplot(plt)

# Impact of Weather on Bike Rentals
st.subheader("Impact of Weather Situation on Bike Rentals")
weather_rental = df1.groupby('weathersit')['cnt'].mean()
plt.figure(figsize=(8, 6))
plt.bar(weather_rental.index, weather_rental.values)
plt.xlabel('Weather Situation (1: Clear, 2: Mist, 3: Light Snow/Rain, 4: Heavy Rain/Snow)')
plt.ylabel('Average Bike Rentals')
plt.title('Impact of Weather on Bike Rentals')
st.pyplot(plt)

# Distribution of Bike Rentals by Weather Situation
st.subheader("Distribution of Bike Rentals by Weather Situation")
plt.figure(figsize=(8, 6))
sns.boxplot(x='weathersit', y='cnt', data=df1)
plt.xlabel('Weather Situation')
plt.ylabel('Total Bike Rentals')
plt.title('Distribution of Bike Rentals by Weather Situation')
st.pyplot(plt)

# Average Bike Rentals by Season and Weather
st.subheader("Average Bike Rentals by Season and Weather")
df1['season_weather'] = df1['season'].astype(str) + '_' + df1['weathersit'].astype(str)
season_weather_rental = df1.groupby('season_weather')['cnt'].mean()

plt.figure(figsize=(12, 6))
season_weather_rental.plot(kind='bar')
plt.xlabel('Season and Weather')
plt.ylabel('Average Bike Rentals')
plt.title('Average Bike Rentals by Season and Weather')
plt.xticks(rotation=45, ha='right')
st.pyplot(plt)

# Identifying Rental Groups
high_rental = season_weather_rental[season_weather_rental > 5000].index.tolist()
medium_rental = season_weather_rental[(season_weather_rental >= 2000) & (season_weather_rental <= 5000)].index.tolist()
low_rental = season_weather_rental[season_weather_rental < 2000].index.tolist()

st.write("Kelompok Penyewaan Tinggi:", high_rental)
st.write("Kelompok Penyewaan Sedang:", medium_rental)
st.write("Kelompok Penyewaan Rendah:", low_rental)
