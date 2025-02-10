A = str(input("Enter the IP Address: "))
segments = A.split('.')

normalized_segments = [str(int(segment)) for segment in segments]
A = '.'.join(normalized_segments)
print(f"IP without leading zeros: {A}")

# output:
# PS D:\MCA1-2\python> python Q7-A.py
# Enter the IP Address: 011.110.001.110
# IP without leading zeros: 11.110.1.110
# PS D:\MCA1-2\python> 