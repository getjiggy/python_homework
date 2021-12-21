import pandas as pd

df = pd.read_csv("C:\\Users\\mattr\\Class\\python_homework\\PyBank\\budget_data.csv")

# getting total number of months
total_number_months = df['Date'].count()

# summing profits/losses
net_profit = df['Profit/Losses'].sum()

# setting variables for iteration
avg_change = 0
max_change = 0
min_change = 0

# setting max_row and min_row to first record for iteration
max_row = df['Date'][1]
min_row = df['Date'][1]

# iterating over df to calculate avg_change, max_change, min_change, max_row, min_row
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
        
# finalizing avg_change        
avg_change /= total_number_months - 1

# printing results
print('Financial Analysis')
print('-----------------------')
print(f'Total Months: {total_number_months}')
print(f'Total Profit: ${round(net_profit)}')
print(f'    Average Change: ${round(avg_change, 2)}')
print(f'Greatest Increase in Profits: {max_row} (${max_change})')
print(f'Greatest Decrease in Profits: {min_row} (${min_change})')
