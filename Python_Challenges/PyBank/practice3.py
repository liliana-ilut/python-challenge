import os
import csv 

filepath = os.path.join("Resources", "budget_data.csv")
output_file = "Financial_Analysis.txt"

with open(filepath, "r") as in_file:
    in_csv = csv.reader(in_file)
    csv_header = next(in_csv)
    # print(f"Header: {csv_header}")

    profit = []
    months = []
    revenue_change = []


    # seperate profit and months using append 
    for row in in_csv:
        profit.append(int(row[1]))
        months.append(row[0])
    
    # calculate total months and total profit 
    total_months = len(months)
    total_profit = sum(profit)
    
    # calculate change in revenue 
    for e in range(1, len(profit)):
        revenue_change.append((int(profit[e]) - int(profit[e-1])))
    
    # calculate average revenue change, greatest increase and greatest decrease 
    revenue_average = sum(revenue_change) / len(revenue_change)
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)
  
    # print out results 
    print("Financial Analysis")
    print("__________________________")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(round(revenue_average, 2)))
    print("Greatest Profit Increase: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Profit Decrease: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

# export text file with financial results 
with open(output_file, "w+") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("__________________________\n")
    text_file.write("\n")
    text_file.write("Total Months: " + str(total_months))
    text_file.write("\n")
    text_file.write("Total: " + "$" + str(total_profit))
    text_file.write("\n")
    text_file.write("Average Change: " + "$" + str(round(revenue_average, 2)))
    text_file.write("\n")
    text_file.write("Greatest Profit Increase: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    text_file.write("\n")
    text_file.write("Greatest Profit Decrease: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

