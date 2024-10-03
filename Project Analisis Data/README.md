# Bike Sharing Dashboard 🛴

An interactive dashboard to analyze and visualize trends in bike-sharing data. This dashboard allows users to filter data, view descriptive statistics, and visualize bike rental trends across seasons, hours of the day, and weather conditions.

## Project Overview

This project based on [bike-sharing dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset) from kaggle. The dataset contains various weather-related and time-based columns to help analyze how different factors affect bike rentals.

The dashboard is built using **Streamlit** to provide an interactive experience where users can explore the data through filters and various visualizations.

## Features

- **Interactive Filtering:** Filter the dataset by seasons and hours of the day.
- **Data Summary:** Display descriptive statistics of weather-related and rental data.
- **Weather Analysis:** Group by weather conditions and visualize their effect on bike rentals.
- **Season and Hour Trends:** Display trends of bike rentals across seasons and hours of the day.

## Dataset

The dataset used in this project is only the `hour.csv` dataset containing records of hourly bike rentals. Each row includes the following columns:
- **instant:** Record index
- **dteday:** Date of the record
- **season:** Season (1 = Spring, 2 = Summer, 3 = Fall, 4 = Winter)
- **yr:** Year (0 = 2011, 1 = 2012)
- **mnth:** Month
- **hr:** Hour of the day
- **holiday:** Whether the day was a holiday
- **weekday:** Day of the week
- **workingday:** Whether the day was a working day (not a weekend or holiday)
- **weathersit:** Weather condition (1 = Clear, 2 = Mist, 3 = Light Snow/Rain, 4 = Heavy Rain)
- **temp:** Normalized temperature in Celsius
- **atemp:** Normalized "feeling" temperature in Celsius
- **hum:** Humidity level
- **windspeed:** Wind speed level
- **casual:** Number of casual (non-registered) users
- **registered:** Number of registered users
- **cnt:** Total number of rentals

## Setup Environment
```bash
pip install -r requirements.txt
```
## Run Streamlit App
```bash
streamlit run mydashboard.py
```

