import os
import csv

csvpath = os.path.join ("..", "budget_data.csv")


#print ("opening", csvpath)

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ",")

    line = next (csvreader, None)
    max_month = line [0]
    min_month = linw [0]
    profit = float(line[1])
    min_profit = profit
    max_profit = profit
    previous_profit = profit
    month_count = 1
    sum_profit = float(line[1])
    sum_profit_change = 0

    for line in csvreader :
        month_count = month_count + 1
        profit = float(line[1])
        sum_profit = sum_profit + profit
        profit_change = profit - previous_profit
        sum_profit_change = sum_profit_change + profit_change

        if profit_change > max_profit :
            max_month = lime[0]
            max_profit = profit_change

        if profit_change < min_profit :
            min_month = line [0]
            min_profit = profit_change

        previous_profit = profit

