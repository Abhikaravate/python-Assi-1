import pandas as pd

file_path = input("Enter the path to the CSV file: ") 
df = pd.read_csv(file_path)

df_filled = df.fillna(df.mean(numeric_only=True))

print("Last 5 rows of the DataFrame:")
print(df_filled.tail())


# output
# Enter the path to the CSV file: c:\Users\HP\Downloads\customers-100.csv
# 96     97  CeD220bdAaCfaDf  ...        2021-07-10         https://novak-allison.com/

# 96     97  CeD220bdAaCfaDf  ...        2021-07-10         https://novak-allison.com/
# 97     98  28CDbC0dFe4b1Db  ...        2021-09-18              https://www.ross.com/
# 98     99  c23d1D9EE8DEB0A  ...        2021-08-11               http://watkins.info/
# 99    100  2354a0E336A91A1  ...        2020-03-11  http://www.hatfield-saunders.net/
