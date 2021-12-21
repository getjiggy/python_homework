#


import pandas as pd

df = pd.read_csv("C:\\Users\\mattr\\Class\\python_homework\\PyBank\\budget_data.csv")

total_number_months = df['Date'].count()

net_profit = df['Profit/Losses'].sum()
change = df['Profit/Losses'][1] - df['Profit/Losses'][0]
avg_change = 0
max_change = 0
max_row = df['Date'][1]
min_row = df['Date'][1]
min_change = 0

for i in df.index:
    if i != total_number_months - 1:
        avg_change += df['Profit/Losses'][i + 1] - df['Profit/Losses'][i]
        if max_change == 0:
            max_change = df['Profit/Losses'][i + 1] - df['Profit/Losses'][i]
            max_row = df['Date'][i + 1]
        elif max_change < df['Profit/Losses'][i + 1] - df['Profit/Losses'][i]:
            max_change = df['Profit/Losses'][i + 1] - df['Profit/Losses'][i]
            max_row = df['Date'][i + 1]
        if min_change == 0:
            min_change = df['Profit/Losses'][i + 1] - df['Profit/Losses'][i]
            min_row = df['Date'][i + 1]
        elif min_change > df['Profit/Losses'][i + 1] - df['Profit/Losses'][i]:
            min_change = df['Profit/Losses'][i + 1] - df['Profit/Losses'][i]
            min_row = df['Date'][i + 1]
    else:
        break
avg_change /= total_number_months - 1

print('Financial Analysis')
print('-----------------------')
print(f'Total Months: {total_number_months}')
print(f'Total Profit: ${round(net_profit)}')
print(f'    Average Change: ${round(avg_change, 2)}')
print(f'Greatest Increase in Profits: {max_row} (${max_change})')
print(f'Greatest Decrease in Profits: {min_row} (${min_change})')
