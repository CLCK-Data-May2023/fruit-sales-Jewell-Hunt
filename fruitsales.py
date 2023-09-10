# add your code here

#importing the module
import pandas as pd

#creating the fruit_sales DataFrame
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas':[21, 34]}, index=['2017 Sales', '2018 Sales'])
print(fruit_sales)

#converting to CSV file
fruit_sales.to_csv('fruit.csv', index = False)