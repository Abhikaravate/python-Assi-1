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
