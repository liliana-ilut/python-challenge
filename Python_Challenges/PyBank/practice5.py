# Dependencies
import csv

# Files to load and output
file_to_load = "raw_data/budget_data.csv"
file_to_output = "analysis/budget_analysis_1.txt"

# track revenue parameters
total_months = 0 
prev_revenue = 0
month_of_change = []
revenue_change_list = [] 
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0 

# read csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    
    for row in reader:

        # track the totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

        # track the revenue change
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change = [row["Date"]]

        # the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # calculate the greates decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# cal. the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

#generate output summary 
output = (
    F"\nFinancial Analysis\n"
    F"--------------------------\n"
    F"Total Months: {total_months}\n"
    F"Total Revenue: ${total_revenue}\n"
    F"Average Revenue Change: ${revenue_avg}\n"
    F"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    F"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)


print(output)

# export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)