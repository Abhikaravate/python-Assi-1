dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Find keys in dict1 but not in dict2
B = dict1.keys() - dict2.keys()

# Print the result
print("Keys in dict1 but not in dict2:" , B )

# output
# python Q17.py
# Keys in dict1 but not in dict2: {'a', 'b'}
