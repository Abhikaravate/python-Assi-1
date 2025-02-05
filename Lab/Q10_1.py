# Demonstrate the following functions/methods which operates on lists in Python with suitable 
# examples: len ( ) ,count( ) ,index ( ),append( ) ,insert( ) ,extend() ,remove( ), pop( ),reverse( ) 
# ,copy( ) 

A = [1,2,3,4,5,6,7,8,9,10,1,1]
B = [10,11,12,13,14,15,16,17,18,19,20]

print("Length:")
print(len(A))
print("Count :")
print(A.count(1))

print("value at index no: ")
print(A.index(5))

print("Append :")
A.append(10)
print(A)

print("Insert :")
B.insert(3,10)
print(B)

print("Remove:")
B.remove(10)
print(B)

print("Extend:")
B.extend([100,200])
print(B)

print("pop:")
B.pop(2)
print(B)

print("Copy:")
A.copy()
print(A)
