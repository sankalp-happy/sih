import pandas as pd

# Load the data
df = pd.read_csv('Atal_Jal_Disclosed_Ground_Water_Level-2015-2022.csv', encoding='ISO-8859-1')

# List of columns to check
columns_to_check = ['Pre-monsoon_2015 (meters below ground level)', 'Post-monsoon_2015 (meters below ground level)', 'Pre-monsoon_2016 (meters below ground level)', 'Post-monsoon_2016 (meters below ground level)', 'Pre-monsoon_2017 (meters below ground level)', 'Post-monsoon_2017 (meters below ground level)', 'Pre-monsoon_2018 (meters below ground level)', 'Post-monsoon_2018 (meters below ground level)', 'Pre-monsoon_2019 (meters below ground level)', 'Post-monsoon_2019 (meters below ground level)', 'Pre-monsoon_2020 (meters below ground level)', 'Post-monsoon_2020 (meters below ground level)', 'Pre-monsoon_2021 (meters below ground level)', 'Post-monsoon_2021 (meters below ground level)', 'Pre-monsoon_2022 (meters below ground level)', 'Post-monsoon_2022 (meters below ground level)']

# drop rows with NaN values in the imp columns
for column in columns_to_check:
    df[column] = pd.to_numeric(df[column], errors='coerce')

df = df.dropna(subset=columns_to_check)
df.to_csv('cleaned_file.csv', index=False)