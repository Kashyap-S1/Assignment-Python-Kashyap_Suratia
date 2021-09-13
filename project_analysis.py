# # Import the required Libraries and data

import pandas as pd
import os
import csv
import sys


budget_data = pd.read_csv("resources/budget_data.csv")
budget_data.head()


# # Data Analysis

# Get the total number of months 
total_months = budget_data['Date'].nunique()
total_months

# Total amount of Profit/Losses overthe entire period 
net_total_ProfitLosses = sum(budget_data["Profit/Losses"])
net_total_ProfitLosses


"""
revenue change = every_item- previous_item
append revenue_change to a profit change list
calculate the average of the profit_change list
"""

reverse_counter = budget_data.shape[0] - 1 #helps us get every item and reverse
profit_change = [] #stores all the changes in the revenue

for item in range(len(budget_data)):
    every_item = budget_data["Profit/Losses"][reverse_counter]
    try:
        previous_item = budget_data["Profit/Losses"][reverse_counter - 1]
    except KeyError:
        break
    
    revenue_change = every_item - previous_item
    profit_change.append(revenue_change)
    
    reverse_counter-=1
    
#calculate the average of a list

# reverse the profit_change list to create a list in correct order
profitLoss_change = profit_change[::-1]
average_revenue_change = round(sum(profitLoss_change)/len(profitLoss_change), 2)
average_revenue_change


# greatest increase in profit is max of the profit change list
greatest_increase_in_profits = max(profitLoss_change)
when_increased = profitLoss_change.index(greatest_increase_in_profits)
date_increased = budget_data["Date"][when_increased + 1]
date_increased


greatest_increase_in_profits


# greatest decrease in profit is max of the profit change list
greatest_decrease_in_profits = min(profitLoss_change)
when_decreased = profitLoss_change.index(greatest_decrease_in_profits)
date_decreased = budget_data["Date"][when_decreased + 1]
date_decreased


greatest_decrease_in_profits


# # Results

PyBank_results = f"""
Financial Analysis
-----------------------------------------
Total Months: {total_months}
Total: ${net_total_ProfitLosses}
Greatest Increase in Profits: {date_increased} (${greatest_increase_in_profits})
Greatest Increase in Profits: {date_decreased} (${greatest_decrease_in_profits})
"""

print(PyBank_results)


with open('PyBank results.txt', 'w') as f:
    f.write(PyBank_results)
