def removeEle(TL):
    return tuple(lst[1:] for lst in TL)

A = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
result = removeEle(A)
print(result) 

 # Output: ([2, 3], [5, 6], [8, 9])
