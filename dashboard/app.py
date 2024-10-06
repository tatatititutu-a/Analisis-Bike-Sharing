import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
df = pd.read_csv('dashboard/main_data.csv')

# Convert 'dteday' to datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Judul Dashboard 
st.title("Bike Rental Analysis Dashboard")

# Visualizing correlation matrix
st.subheader("Correlation Matrix")
correlation_matrix = df.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Main Data')
st.pyplot(plt)
plt.clf()  # Clear the figure after displaying

# Visualizing bike rentals per day
st.subheader("Histogram of Bike Rentals per Day")
plt.figure(figsize=(10, 6))
plt.hist(df['cnt'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Total Bike Rentals')
plt.ylabel('Frequency')
plt.title('Histogram of Bike Rentals per Day')
st.pyplot(plt)
plt.clf()  # Clear the figure after displaying

# Analysis of bike rentals by season
st.subheader("Box Plot of Bike Rentals by Season")
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=df, palette='Set3')
plt.xlabel('Season')
plt.ylabel('Total Bike Rentals')
plt.title('Box Plot of Bike Rentals by Season')
st.pyplot(plt)
plt.clf()  # Clear the figure after displaying

# Impact of Holiday on Bike Rentals
st.subheader("Impact of Holiday on Bike Rentals")
holiday_rental = df.groupby('holiday')['cnt'].mean()
plt.figure(figsize=(8, 6))
plt.bar(holiday_rental.index, holiday_rental.values, color='lightgreen')
plt.xlabel('Holiday (0: No, 1: Yes)')
plt.ylabel('Average Bike Rentals')
plt.title('Impact of Holiday on Bike Rentals')
st.pyplot(plt)
plt.clf()  # Clear the figure after displaying

# Impact of Weather on Bike Rentals
st.subheader("Impact of Weather Situation on Bike Rentals")
weather_rental = df.groupby('weathersit')['cnt'].mean()
plt.figure(figsize=(8, 6))
plt.bar(weather_rental.index, weather_rental.values, color='lightblue')
plt.xlabel('Weather Situation (1: Clear, 2: Mist, 3: Light Snow/Rain, 4: Heavy Rain/Snow)')
plt.ylabel('Average Bike Rentals')
plt.title('Impact of Weather on Bike Rentals')
st.pyplot(plt)
plt.clf()  # Clear the figure after displaying

# Distribution of Bike Rentals by Weather Situation
st.subheader("Distribution of Bike Rentals by Weather Situation")
plt.figure(figsize=(8, 6))
sns.boxplot(x='weathersit', y='cnt', data=df)
plt.xlabel('Weather Situation')
plt.ylabel('Total Bike Rentals')
plt.title('Distribution of Bike Rentals by Weather Situation')
st.pyplot(plt)
plt.clf()  # Clear the figure after displaying

# Average Bike Rentals by Season and Weather
st.subheader("Average Bike Rentals by Season and Weather")
df['season_weather'] = df['season'].astype(str) + '_' + df['weathersit'].astype(str)
season_weather_rental = df.groupby('season_weather')['cnt'].mean()

plt.figure(figsize=(12, 6))
season_weather_rental.plot(kind='bar', color='salmon')
plt.xlabel('Season and Weather')
plt.ylabel('Average Bike Rentals')
plt.title('Average Bike Rentals by Season and Weather')
plt.xticks(rotation=45, ha='right')
st.pyplot(plt)
plt.clf()  # Clear the figure after displaying

# Identifying Rental Groups
high_rental = season_weather_rental[season_weather_rental > 5000].index.tolist()
medium_rental = season_weather_rental[(season_weather_rental >= 2000) & (season_weather_rental <= 5000)].index.tolist()
low_rental = season_weather_rental[season_weather_rental < 2000].index.tolist()

st.write("Kelompok Penyewaan Tinggi:", high_rental)
st.write("Kelompok Penyewaan Sedang:", medium_rental)
st.write("Kelompok Penyewaan Rendah:", low_rental)
