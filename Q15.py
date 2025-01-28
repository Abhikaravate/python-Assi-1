year = int(input("Enter the year"))
if year < 0:
    print("invalid input check it ")
else:    
    if year % 4 == 0:
          print("Year is leap year ")
    else:
         print("its not leap year")

# Output
# PS D:\MCA1-2\python> python Q15.py
# Enter the year -2
# invalid input check it 
# PS D:\MCA1-2\python> python Q15.py
# Enter the year 2024
# Year is leap year 
# PS D:\MCA1-2\python>          