A = str(input("Enter the IP Address: "))
segments = A.split('.')

normalized_segments = [str(int(segment)) for segment in segments]
A = '.'.join(normalized_segments)
print(f"IP without leading zeros: {A}")
