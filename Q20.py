A = input("Enter the string")
b = ''.join([char for char in A[::-1] if char.lower() != 's'])
print(b)
# output
# PS D:\MCA1-2\python> & C:/Users/HP/AppData/Local/Programs/Python/Python313/python.exe d:/MCA1-2/python/Q20.py
# Enter the string  abscd
# dcba
# PS D:\MCA1-2\python> 