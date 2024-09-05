import pandas as pd

# Load the data
df = pd.read_csv('trimmed_monthly_mean2.csv')


# Load the transposed DataFrame
df1 = pd.read_csv('transposed.csv')

# Load the second DataFrame
df2 = pd.read_csv('pune3.csv')

# Add a temporary key to both DataFrames to perform the cross join
df1['key'] = 0
df2['key'] = 0

# Perform the cross join
merged_df = pd.merge(df1, df2, how='outer', on='key')

# Drop the temporary key column
merged_df.drop('key', axis=1, inplace=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged.csv', index=False)