def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()  # Move to the next line after printing the series

# Example usage
num = int(input("Enter a number: "))
fibonacci(num)
