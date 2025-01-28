import numpy as np 
import pandas as pd

array = np.array([[1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5]])
print(array)
print("2*2 array")
bf = array[-2:, -2:]
print(bf)

# output
# PS D:\MCA1-2\python> python Q14.py
# [[1 2 3 4 5]
#  [1 2 3 4 5]
#  [1 2 3 4 5]
#  [1 2 3 4 5]
#  [1 2 3 4 5]]
# 2*2 array
# [[4 5]
#  [4 5]]