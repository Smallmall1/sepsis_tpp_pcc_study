
import pandas as pd
import numpy as np

# Read the data from a CSV file into a Pandas DataFrame
pd.read_csv("/Users/data.csv")
df=pd.read_csv("/Users/data.csv")

# Create a new column 'map_ventile' by dividing the 'map' column into 20 quantiles and labeling each record with the quantile number (0 to 19)
df['map_ventile'] = pd.qcut(df['map'], q=20, labels=False)

#Create a new column 'pcc_quintile_within_map_ventile' by dividing the 'pcc' column into 5 quantiles within each 'map_ventile' group
df['pcc_quintile_within_map_ventile'] = df.groupby('map_ventile')['pcc'].transform(lambda x: pd.qcut(x, q=5, labels=False))

# Create a new column 'Group' which is a combination of 'map_ventile' and 'pcc_quintile_within_map_ventile'
df['Group'] = df['map_ventile'].astype(str) + '_' + df['pcc_quintile_within_map_ventile'].astype(str)

# Print the DataFrame with the new columns
print(df)

# Count the number of records in each group formed by the combination of 'map_ventile' and 'pcc_quintile_within_map_ventile'
num_groups = df.groupby(['map_ventile', 'pcc_quintile_within_map_ventile']).size()
print(num_groups)

# Save the DataFrame with the new columns to a CSV file
df.to_csv("/Users/data.csv", index=False)
