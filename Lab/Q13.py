my_dict = {'name': 'Abhi', 'age': 25, 'city': 'pune'}

copy_dict = my_dict.copy()
 
print("Get 'name':", my_dict.get('name')) 
print("Get 'country' (not in dict):", my_dict.get('country', 'Not Found'))  

age = my_dict.pop('age')

print("Popped 'age':", age)
print("Dictionary after pop:", my_dict) 

dict_copy = my_dict.copy()

print("Copied dictionary:", dict_copy)  
print("Keys:", my_dict.keys()) 
print("Values:", my_dict.values()) 
print("Items:", my_dict.items())  

copy_dict.clear()
print("After clear():", copy_dict)

# output
# Get 'name': Abhi
# Get 'country' (not in dict): Not Found
# Popped 'age': 25
# Dictionary after pop: {'name': 'Abhi', 'city': 'pune'}
# Copied dictionary: {'name': 'Abhi', 'city': 'pune'}
# Keys: dict_keys(['name', 'city'])
# Values: dict_values(['Abhi', 'pune'])
# Items: dict_items([('name', 'Abhi'), ('city', 'pune')])
# After clear(): {}