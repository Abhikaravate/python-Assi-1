def sumn(n):
     if n == 1:  # Base case
        return 1
     return n + sumn(n - 1)

n =  int(input("Enter the value of n  "))
sumn(n)
print( "The sum is ", sumn(n))
print(f"The sum of the first {n} natural numbers is: {sumn(n)}")

# output
# PS D:\MCA1-2\python> python Q16.py
# Enter the value of n  10
# The sum is  55