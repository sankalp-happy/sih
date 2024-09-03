import pandas as pd

# Load the data

# Load the data
df = pd.read_csv('pune2.csv')

# Define the identifier variables
id_vars = ['Sr. No.', 'State_Name_With_LGD_Code', 'DISTRICT', 'Block_Name_With_LGD_Code', 'GP_Name_With_LGD_Code', 'Village', 'Site_Name', 'TYPE', 'SOURCE', 'Well_ID', 'Latitude', 'Longitude', 'Well_Depth (meters)', 'Aquifer', 'STATE_UT_NAME', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'ANNUAL', 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec']

# Reshape the DataFrame
df_melted = df_melted[df_melted['Year_Monsoon'].str.contains(r'^\d{4}_\w+$')]

# Split the 'Year_Monsoon' column into 'Monsoon' and 'Year' columns
df_melted[['Monsoon', 'Year']] = df_melted['Year_Monsoon'].str.split('_', expand=True)

# Convert the 'Year' column to numeric
df_melted['Year'] = pd.to_numeric(df_melted['Year'])

# Sort the DataFrame by the Year column
df_sorted = df_melted.sort_values('Year')

# Save the sorted DataFrame to a new CSV file
df_sorted.to_csv('pune2_sorted.csv', index=False)