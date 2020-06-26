import os
import csv

#set the path for the csv file
mainpath_csv = os.path.join ("budget_data.csv")

#output file for the analysis text
output_file = "Financial_Analysis.txt"

#open and read csv file
with open(mainpath_csv, "r") as csvfile :
    reader = csv.reader(csvfile, delimiter = ',')

    #read the header row first
    csv_header = next(csvfile)

    #print the header to check if code works before moving on and mark it as a comment so it won't interact with the actual code
    #print(f"Header: {csv_header}")

months = []
profit = []
change = []

# read through each row of data after header
for row in reader :
        profit.append(int(row[1]))
        months.append(row[0])

#calculate total months and total profit/Losses

total_months = len(months)
total_profit = sum(profit)

# calculate the change in revenue 
for i in range(1, len(profit)):
    revenue_change.append((int(profit[i]) - int(profit[i-1])))

print("Financial Analysis")
print("__________________________")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(round(revenue_average, 2)))
print("Greatest Profit Increase: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
print("Greatest Profit Decrease: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))
