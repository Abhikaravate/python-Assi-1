def sum_inner_tuples(tuple_of_tuples):
    return sum(sum(tpl) for tpl in tuple_of_tuples)

my_tuple = [(1, 2), (3, 4), (5, 6)]  
result = sum_inner_tuples(my_tuple)

print(result)

# Output: 21
