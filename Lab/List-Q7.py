def sortS(TL):
    return tuple(sorted(lst) for lst in TL)
A= ([3, 1, 2], [9, 7, 8], [6, 5, 4])
result = sortS(A)
print(result)  

# Output: ([1, 2, 3], [7, 8, 9], [4, 5, 6])
