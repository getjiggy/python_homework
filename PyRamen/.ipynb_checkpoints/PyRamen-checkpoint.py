# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('C:\\Users\\mattr\\Class\\python_homework\\PyRamen\\Resources\\menu_data.csv')
sales_filepath = Path('C:\\Users\\mattr\\Class\\python_homework\\PyRamen\\Resources\\sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as menu_csv:
    reader = csv.reader(menu_csv)
    next(reader)
    for row in reader:
        menu.append(row)









# @TODO: Read in the sales data into the sales list


with open(sales_filepath, 'r') as sales_csv:
    reader = csv.reader(sales_csv)
    next(reader)
    for row in reader:
        sales.append(row)







# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0
print(sales[1])
print(menu[1])
# @TODO: Loop over every row in the sales list object
for i in range(len(sales)):
    quantity = sales[i][3]
    sales_item = sales[i][4]
    if sales_item not in report:
        report[sales_item] = {'01-count': 0,
                             '02-revenue': 0,
                             '03-cogs':0,
                             '04-profit':0}
    for i in range(len(menu)):
        menu_item = menu[i][0]
        price = menu[i][3]
        cost = menu[i][4]
        if sales_item == menu_item:
            profit = float(quantity) * (float(price) - float(cost))
            report[sales_item]['01-count'] += float(quantity)
            report[sales_item]['02-revenue'] += float(price) * float(quantity)
            report[sales_item]['03-cogs'] += float(cost) * float(quantity)
            report[sales_item]['04-profit'] += float(profit) * float(quantity)
        else:
            print(f'{sales_item} does not equal {menu_item}! NO MATCH!')
with open('report.txt', 'w') as text:
    text.write(str(report))