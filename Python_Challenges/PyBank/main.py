import os
import csv 

    #set the path for the csv file
csv_path = os.path.join("Resources", "budget_data.csv")

    #print the path to make sure the path opens correctly. Mark the print in a cooment so it won't interact with our main code
#print ("opening", csv_path)

    #open and read the csv file
with open(csv_path, "r") as in_file:
    csv_reader = csv.reader(in_file)

    #read first row's header and print the header to make sure it work, after that mark it as a comment so it won't interact with our code
    csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")

    #creates lists to store data
    pro_los = []
    months = []
    revenue_change = []

    # seperate profit/losses and months using append 
    for row in csv_reader:
        pro_los.append(int(row[1]))
        months.append(row[0])
    
    # calculate total months and total profit/losses
    total_months = len(months)
    total_pro_los = sum(pro_los)
    
    # calculate change in revenue 
    for i in range(1, len(pro_los)):
        revenue_change.append((int(pro_los[i]) - int(pro_los[i-1])))
    
    # calculate average revenue change, greatest increase in profit and greatest decrease in losses
    average_change = sum(revenue_change) / len(revenue_change)
    great_increase_profit = max(revenue_change)
    great_decrease_loss = min(revenue_change)
  

   #print the results in the terminal
   #create a separate text file with the results/analysis
with open("financial analysis.txt", "w") as text_file :
    print("financial analysis", file = text_file)
    print("__________________________", file = text_file)
    print("Total Months : " + str(total_months) , file = text_file)
    print("Total Profit/Losses : " + "$" + str(total_pro_los) , file = text_file)
    print("Average Change : " + "$" + str(round(average_change, 2)) , file = text_file)
    print("Greatest Increase in Profit : " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(great_increase_profit) , file = text_file)
    print("Greatest Decrease in profit : " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(great_decrease_loss) , file = text_file)

with open("financial analysis.txt", "r") as text_file:
    print(text_file.read())