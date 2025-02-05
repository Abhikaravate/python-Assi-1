arr = input("Enter Elements of Array: ").split()
print("Your array:", arr)


arr = list(map(int, arr))  

n = len(arr)
positive = []
negative = [] 

for i in range(n):
    if arr[i] > 0:
        positive.append(arr[i])  
    else:
        negative.append(arr[i])  

print("Positive numbers:", positive)
print("Negative numbers:", negative)
