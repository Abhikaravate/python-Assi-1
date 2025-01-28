import pandas as pd
import numpy as np

data = {
    "City": ["Delhi", "Bengaluru", "Chennai", "Mumbai", "Kolkata"],
    "MaxTemp": [40, 31, 35, 29, 39],
    "MinTemp": [32, 25, 27, 21, 23],
    "RainFall": [24.1, 36.2, 40.8, 35.2, 41.8]
}

df = pd.DataFrame(data)


sum_columns = df.select_dtypes(include=np.number).sum()

# ii) Compute mean of the RainFall column
mean_rainfall = df["RainFall"].mean()

# iii) Compute median of the MaxTemp column
median_maxtemp = df["MaxTemp"].median()

# iv) Display all column names
column_names = df.columns.tolist()

# Display results
print("Sum of numeric columns:")
print(sum_columns)
print("\nMean of RainFall column:", mean_rainfall)
print("\nMedian of MaxTemp column:", median_maxtemp)
print("\nColumn Names:", column_names)

# Output
# PS D:\MCA1-2\python> python Q10.py
# Sum of numeric columns:
# MaxTemp     174.0
# MinTemp     128.0
# RainFall    178.1
# dtype: float64

# Mean of RainFall column: 35.620000000000005

# Median of MaxTemp column: 35.0

# Column Names: ['City', 'MaxTemp', 'MinTemp', 'RainFall']