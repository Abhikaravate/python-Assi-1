import pandas as pd

path = input("Enter the Csv file path ")
df = pd.read_csv(path)

filled = df.fillna(df.mean(numeric_only=True))
print("frist 10 Coloums ")
print(filled.head(10))
print("All Coloums")
print(filled.all)



# output
# Enter the Csv file path c:\Users\HP\Downloads\customers-100.csv
#    Index      Customer Id  ... Subscription Date                      Website
# 0      1  DD37Cf93aecA6Dc  ...        2020-08-24   http://www.stephenson.com/
# 1      2  1Ef7b82A4CAAD10  ...        2021-04-23        http://www.hobbs.com/
# 2      3  6F94879bDAfE5a6  ...        2020-03-25     http://www.lawrence.com/
# 3      4  5Cef8BFA16c5e3c  ...        2020-06-02   http://www.good-lyons.com/
# 4      5  053d585Ab6b3159  ...        2021-04-17  https://goodwin-ingram.com/
# 5      6  2d08FB17EE273F4  ...        2020-02-25       http://www.berger.net/
# 6      7  EA4d384DfDbBf77  ...        2021-08-24          https://www.le.com/
# 7      8  0e04AFde9f225dE  ...        2021-04-12  https://hammond-ramsey.com/
# 8      9  C2dE4dEEc489ae0  ...        2020-01-13     https://www.bullock.net/
# 9     10  8C2811a503C7c5a  ...        2021-11-08           https://arias.com/
# [10 rows x 12 columns]
# All Coloums
# <bound method DataFrame.all of     Index      Customer Id  ... Subscription Date                            Website
# 0       1  DD37Cf93aecA6Dc  ...        2020-08-24         http://www.stephenson.com/
# 1       2  1Ef7b82A4CAAD10  ...        2021-04-23              http://www.hobbs.com/
# 2       3  6F94879bDAfE5a6  ...        2020-03-25           http://www.lawrence.com/
# 3       4  5Cef8BFA16c5e3c  ...        2020-06-02         http://www.good-lyons.com/
# 4       5  053d585Ab6b3159  ...        2021-04-17        https://goodwin-ingram.com/
# ..    ...              ...  ...               ...                                ...
# 95     96  cb8E23e48d22Eae  ...        2022-01-30            http://hayes-perez.com/
# 96     97  CeD220bdAaCfaDf  ...        2021-07-10         https://novak-allison.com/
# 97     98  28CDbC0dFe4b1Db  ...        2021-09-18              https://www.ross.com/
# 98     99  c23d1D9EE8DEB0A  ...        2021-08-11               http://watkins.info/
# 99    100  2354a0E336A91A1  ...        2020-03-11  http://www.hatfield-saunders.net/

# [100 rows x 12 columns]>
