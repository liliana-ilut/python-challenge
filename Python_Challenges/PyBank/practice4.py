import os
import csv

# File List
budget_data = ['1', '2']

#Create variables 
month_counter = 0
total_revenue = 0
total_revenue_change = 0

# Loop through files
for files in budget_data:
    # Get CSV
    budget_data = os.path.join("C:/Users/lhern/Documents/Python Original/Python Homework/PyBank/Resources/budget_data.csv")


    # Open csv file
    with open(budget_data) as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skip the first line (headers)
        next(csvReader, None)
        
    
        # Get data 
        line = next(csvReader,None)
        max_month = line[0]
        min_month = line[0]
        revenue = float(line[1])
        min_revenue = revenue
        max_revenue = revenue
        previous_revenue = revenue
        month_counter = 1
        total_revenue = float(line[1])
        total_revenue_change = 0

        # Read one line at a time
        for line in csvReader:

            # Find total months
            month_counter = month_counter + 1

            revenue = float(line[1])

            # Add to find total revenue (one month at a time) 
            total_revenue = total_revenue + revenue

            # Find month over months change in revenue 
            revenue_change = revenue - previous_revenue

            # Add total revenue change
            total_revenue_change = total_revenue_change + revenue_change

            # Find min and max revenue change 
            if revenue_change > max_revenue:
                max_month = line[0]
                max_revenue = revenue_change

            if revenue_change < min_revenue:
                min_month = line[0]
                min_revenue = revenue_change

            # Set previous revenue 
            previous_revenue = revenue

        # Finish calculations
        average_revenue = total_revenue/month_counter
        average_revenue_change = total_revenue_change/(month_counter-1)

        # Round decimal
        total_revenue = int(total_revenue)
        average_revenue_change = int(average_revenue_change)
        max_revenue = int(max_revenue)
        min_revenue = int(min_revenue)
        
        # Print analysis
        print(f"Financial Analysis:")
        print("-------------------------------------------------------")
        print(f"Total Months: {month_counter}")
        print(f"Total Revenue: {total_revenue} USD")
        print(f"Average Revenue Change: {average_revenue_change} USD")
        print(f"Greatest Increase in Revenue: {max_month} {max_revenue} USD")
        print(f"Greatest Decrease in Revenue: {min_month} {min_revenue} USD")
        print("")
        
        # Name white file
        output_file = budget_data[0:-4]

        write_budget_data = f"{output_file}_pybank_results.txt"

        # Open write file
        filewriter = open(write_budget_data, mode = 'w')

        # Print to write file
        filewriter.write(f"Financial Analysis:\n")
        filewriter.write("-------------------------------------------------------\n")
        filewriter.write(f"Total Months: {month_counter}\n")
        filewriter.write(f"Total Revenue: {total_revenue} USD\n")
        filewriter.write(f"Average Revenue Change: {average_revenue_change} USD\n")
        filewriter.write(f"Greatest Increase in Revenue: {max_month} {max_revenue} USD\n")
        filewriter.write(f"Greatest Decrease in Revenue: {min_month} {min_revenue} USD\n")
        filewriter.write("")

        filewriter.close()