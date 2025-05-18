# Uber Case Study: Exploratory Data Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('./data/uber_data.csv')
df = data.copy()

# Data Overview
print('First 5 rows:')
print(df.head())

print('Last 5 rows:')
print(df.tail())

print('\nShape:', df.shape)
print('\nInfo:')
df.info()
print('\nStatistical Summary:')
print(df.describe().T)

# Unique values in categorical columns
print('\nUnique boroughs:', df['borough'].unique())
print('\nHoliday value counts:')
print(df['hday'].value_counts(normalize=True))

# Fixing datatypes
print('\nConverting pickup_dt to datetime...')
df['pickup_dt'] = pd.to_datetime(df['pickup_dt'], format="%d-%m-%Y %H:%M")
df['start_year'] = df.pickup_dt.dt.year
df['start_month'] = df.pickup_dt.dt.month_name()
df['start_hour'] = df.pickup_dt.dt.hour
df['start_day'] = df.pickup_dt.dt.day
df['week_day'] = df.pickup_dt.dt.day_name()
df.drop('pickup_dt', axis=1, inplace=True)
print(df.head())

# Missing value treatment
print('\nMissing values:')
print(df.isnull().sum())
df['borough'].fillna('Unknown', inplace=True)
df['temp'] = df['temp'].fillna(value=df.loc[(df['borough'] == 'Brooklyn') & (df['start_month'] == 'January') & (df['start_day'] >= 16),'temp'].mean())
print('Missing values after treatment:')
print(df.isnull().sum())

# Univariate Analysis
sns.histplot(data=df, x='pickups')
plt.title('Distribution of Pickups')
plt.show()
sns.boxplot(data=df, x='pickups')
plt.title('Boxplot of Pickups')
plt.show()

# ... (Repeat for other variables as in the notebook)

# Bivariate Analysis: Correlation Heatmap
num_var = data.dtypes[data.dtypes != 'object'].index
corr = df[num_var].corr(numeric_only=True)
plt.figure(figsize=(15, 7))
sns.heatmap(corr, annot=True, vmin=-1, vmax=1, fmt=".2f", cmap="Spectral")
plt.title('Correlation Heatmap')
plt.show()

# Actionable Insights and Recommendations
print("""
Insights:
1. Uber cabs are most popular in the Manhattan area of New York
2. Weather conditions do not have much impact on the number of Uber pickups
3. The demand for Uber has been increasing steadily over the months (Jan to June)
4. The rate of pickups is higher on the weekends as compared to weekdays
5. Demand peaks at 7-8 PM and during office commute hours
6. Further investigation needed for low demand on Mondays

Recommendations:
1. Focus on Manhattan, but also grow Brooklyn, Queens, and Bronx
2. Ensure cab availability during peak hours and Saturday nights
3. Procure more data for fleet size and pricing to optimize operations
4. Build predictive models for demand and pricing
""")
