import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


hour_df = pd.read_csv("main_data.csv")

st.title("Bike Sharing Dashboard🛴")
st.write("An interactive dashboard to analyze the bike-sharing dataset and visualize trends.")

# Add description or explanatory notes for season and weather conditions
st.markdown("""
### Season Explanation:
- **1** = Spring
- **2** = Summer
- **3** = Fall
- **4** = Winter

### Weather Situation Explanation:
- **1** = Clear, Few clouds, Partly cloudy
- **2** = Mist + Cloudy, Mist + Broken clouds
- **3** = Light Snow, Light Rain, Thunderstorm
- **4** = Heavy Rain + Ice Pellets, Thunderstorm, Snow
""")

# Sidebar for filtering
st.sidebar.header("Filter options")
season_filter = st.sidebar.multiselect(
    "Select season(s) to display:",
    options=hour_df['season'].unique(),
    default=hour_df['season'].unique()
)

hour_filter = st.sidebar.slider(
    "Select hour of the day:",
    min_value=int(hour_df['hr'].min()),
    max_value=int(hour_df['hr'].max()),
    value=(int(hour_df['hr'].min()), int(hour_df['hr'].max()))
)

# Filter dataset based on sidebar inputs
filtered_df = hour_df[
    (hour_df['season'].isin(season_filter)) & 
    (hour_df['hr'].between(hour_filter[0], hour_filter[1]))
]

# Display the filtered dataset
st.write(f"Filtered dataset: {len(filtered_df)} records")
st.dataframe(filtered_df.head())

# Group by weather and visualize average rentals
st.subheader("Average Bike Rentals by Weather Condition")

weather_effect = filtered_df.groupby('weathersit')['cnt'].mean().sort_values(ascending=False)
st.write(weather_effect)

# Create a bar chart for weather conditions
fig, ax = plt.subplots()
weather_effect.plot(kind='bar', ax=ax)
ax.set_title("Average Bike Rentals by Weather Condition")
ax.set_xlabel("Weather Condition")
ax.set_ylabel("Average Rentals")
st.pyplot(fig)

# Group by season and hour to visualize trends across seasons
st.subheader("Average Bike Rentals by Season and Hour")

season_hour_trend = filtered_df.groupby(['season', 'hr'])['cnt'].mean().reset_index()
fig, ax = plt.subplots()
sns.lineplot(data=season_hour_trend, x='hr', y='cnt', hue='season', ax=ax)
ax.set_title("Average Bike Rentals by Season and Hour")
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Average Rentals")
st.pyplot(fig)

# Display descriptive statistics
st.subheader("Statistics")
weather_summary = filtered_df[['temp', 'hum', 'windspeed', 'cnt']].describe()
st.write(weather_summary)

# Interactive Scatter plot: Rentals vs Temperature, Humidity, and Windspeed
st.subheader("Scatter Plot: Total Rentals vs Weather Conditions")

# Scatter plot for rentals vs temperature, humidity, and windspeed
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Total Rentals vs Temperature")
    fig1, ax1 = plt.subplots()
    sns.scatterplot(data = filtered_df, x = 'temp', y = 'cnt', ax = ax1)
    ax1.set_title("Rentals vs Temperature")
    st.pyplot(fig1)

with col2:
    st.write("Total Rentals vs Humidity")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data = filtered_df, x = 'hum', y = 'cnt', ax = ax2)
    ax2.set_title("Rentals vs Humidity")
    st.pyplot(fig2)

with col3:
    st.write("Total Rentals vs Windspeed")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data = filtered_df, x = 'windspeed', y = 'cnt', ax = ax3)
    ax3.set_title("Rentals vs Windspeed")
    st.pyplot(fig3)
