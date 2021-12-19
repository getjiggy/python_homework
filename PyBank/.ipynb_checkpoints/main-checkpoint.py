import pandas as pd

df = pd.read_csv("C:\\Users\\mattr\\Class\\python_homework\\PyBank\\budget_data.csv")

total_number_months = 0
net_profit = df['Profit/Losses'].sum()
change = df['Profit/Losses'][1] - df['Profit/Losses'][0]
avg_change = 0
max_change = 0
max_row = df['Date'][1]
min_row = df['Date'][1]
min_change = 0
for index, row in df.iterrows():
    total_number_months += 1
    try: 
        avg_change += df['Profit/Losses'][index + 1] - df['Profit/Losses'][index]
        if max_change == 0:
            max_change = df['Profit/Losses'][index + 1] - df['Profit/Losses'][index]
            max_row = df['Date'][index + 1]
        elif max_change < df['Profit/Losses'][index + 1] - df['Profit/Losses'][index]:
            max_change = df['Profit/Losses'][index + 1] - df['Profit/Losses'][index]
            max_row = df['Date'][index + 1]
        if min_change == 0:
            min_change = df['Profit/Losses'][index + 1] - df['Profit/Losses'][index]
            min_row = df['Date'][index + 1]
        elif min_change > df['Profit/Losses'][index + 1] - df['Profit/Losses'][index]:
            min_change = df['Profit/Losses'][index + 1] - df['Profit/Losses'][index]
            min_row = df['Date'][index + 1]
            print(f"index: {index}, row: {row}, change: {df['Profit/Losses'][index + 1] - df['Profit/Losses'][index]}")
    except:
        continue
avg_change /= total_number_months - 1

print('Financial Analysis')
print('-----------------------')
print(f'Total Months: {total_number_months}')
print(f'Total Profit: ${round(net_profit)}')
print(f'    Average Change: ${round(avg_change, 2)}')
print(f'Greatest Increase in Profits: {max_row} (${max_change})')
print(f'Greatest Decrease in Profits: {min_row} (${min_change})')




