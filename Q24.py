from datetime import datetime

# Get the current date and time
now = datetime.now()

# Lambda functions to extract values
extract_year = lambda dt: dt.year
extract_month = lambda dt: dt.month
extract_day = lambda dt: dt.day
extract_time = lambda dt: dt.strftime("%H:%M:%S")  # Extract time in HH:MM:SS format

# Example usage
print("Year:", extract_year(now))    # Output: Current Year
print("Month:", extract_month(now))  # Output: Current Month
print("Date:", extract_day(now))     # Output: Current Date
print("Time:", extract_time(now))    # Output: Current Time
