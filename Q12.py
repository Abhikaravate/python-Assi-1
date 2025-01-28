
import numpy as np
import pandas as pd

# Create a NumPy array
array = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Convert the NumPy array into a Pandas Series
series = pd.Series(array)

# Find the frequency count of unique items
frequency_count = series.value_counts()

# Display the frequency count
print("Frequency count of unique items:")
print(frequency_count)

# output
# PS D:\MCA1-2\python> python Q12.py
# Frequency count of unique items:
# 4    4
# 3    3
# 2    2
# 1    1
# Name: count, dtype: int64