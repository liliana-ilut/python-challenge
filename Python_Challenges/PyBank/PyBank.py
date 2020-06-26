import os
import csv

csvpath = os.path.join ("..", "budget_data.csv")


#print ("opening", csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ",")

    #print(csvreader)

    #for row in csvreader :
        #print (row [0], row [1])

        #if csv.Sniffer().has_header :
            #next (csvreader)
        #for row in csvreader :
            #count_of_months += 1
#print ("count_of_months")
