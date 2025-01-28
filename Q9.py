import pandas as pd

# Corrected file path using a raw string
file_path = 'C:\Users\HP\Downloads\Sample-Spreadsheet-10-rows.csv'

df = pd.read_csv(file_path)

# i) Display a list of all columns
columns = df.columns.tolist()
print("\nList of columns:", columns)

# ii) Display data with the last three rows and first three columns
last_three_first_three = df.iloc[-3:, :3]
print("\nLast three rows and first three columns:")
print(last_three_first_three)

# output
#  python Q9.py
# List of columns: ['1', 'Abhijeet', 'Unnamed: 2', '3', '-213.25', '38.94', '35', 'Nunavut', 'Storage & Organization', '0.8']

# Last three rows and first three columns:
#     1 Abhijeet  Unnamed: 2
# 6   8  dheeraj         NaN
# 7   9    nitin         NaN
# 8  10   vedant         NaN