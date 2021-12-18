import pandas as pd

df = pd.read_csv("C:\\Users\\mattr\\Class\\python_homework\\PyBank\\budget_data.csv")

total_number_months = 0
net_profit = df['Profit/Losses'].sum()

print(net_profit)
for index, row in df.iterrows():
    total_number_months += 1
    
print(total_number_months)


