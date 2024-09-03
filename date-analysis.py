import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('pune.csv')

# Convert the date column to datetime format
df['date_time'] = pd.to_datetime(df['date_time'], format='%Y-%m-%d %H:%M:%S')


# Set the date column as the DataFrame index
df.set_index('date_time', inplace=True)
df = df.select_dtypes(include=[np.number])
# Resample the DataFrame to a monthly frequency, calculating the mean for each month
df_monthly_mean = df.resample('M').mean()

# Write the resulting DataFrame to a new CSV file
df_monthly_mean.to_csv('monthly_mean.csv')