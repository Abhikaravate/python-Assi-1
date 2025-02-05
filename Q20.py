A = input("Enter the string")
b = ''.join([char for char in A[::-1] if char.lower() != 's'])
print(b)