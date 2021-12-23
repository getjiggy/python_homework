import csv

# set empty record list
record_list = []

# opening budget_data.csv and appending each line to record_list
with open('budget_data.csv') as data:
    csv_reader = csv.reader(data)
    next(csv_reader)
    for line in csv_reader:
        record_list.append(line)

# setting variables for iteration
avg_change = 0
max_change = 0
min_change = 0
net_profit = 0
min_row = ''
max_row = ''        
total_number_months = len(record_list)

# iterating over record_list
for i in range(len(record_list)):
    if i != total_number_months - 1:
        current_change = int(record_list[i + 1][1]) - int(record_list[i][1])
        current_row = record_list[i][0]
        net_profit += current_change
        avg_change += current_change        
        if max_change == 0:
            max_change = current_change
            max_row = current_row
        elif max_change < current_change:
            max_change = current_change
            max_row = current_row
        if min_change == 0:
            min_change = current_change
            min_row = current_row
        elif min_change > current_change:
            min_change = current_change
            min_row = current_row
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