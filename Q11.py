import numpy as np

# Create a 4×3 numpy array
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])

# Find the column-wise mean
column_wise_mean = np.mean(array, axis=0)

print("Array:")
print(array)
print("\nColumn-wise Mean:")
print(column_wise_mean)

# output
# PS D:\MCA1-2\python> python Q11.py
# Array:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Column-wise Mean:
# [5.5 6.5 7.5]