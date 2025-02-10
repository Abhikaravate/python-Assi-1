def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()  # Move to the next line after printing the series

# Example usage
num = int(input("Enter a number: "))
fibonacci(num)

# PS D:\MCA1-2\python> python Q19.py 
# Enter a number: 10
# 0 1 1 2 3 5 8
