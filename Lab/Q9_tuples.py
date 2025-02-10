
numbers_tuple = ((2, 3), (4, 5), (6, 7), (8, 9))


total_sum = sum(sum(inner_tuple) for inner_tuple in numbers_tuple)


print("Sum of all numbers:", total_sum)
