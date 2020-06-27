import os
import csv

    #set the path for the csv file
csv_path = os.path.join("Resources", "election_data.csv")

    #print the path to make sure the path opens correctly. Mark the print in a cooment so it won't interact with our main code
#print ("opening", csv_path)

    #output file for the analysis text
output_file = "election_results/analysis.txt"

    #open and read the csv file
with open(csv_path, "r") as in_file:
    csv_reader = csv.reader(in_file)

    #read first row's header and print the header to make sure it work, after that mark it as a comment so it won't interact with our code
    csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")


    Votes_T = 0
    Votes_K = 0
    Votes_C = 0 
    Votes_Li = 0
    Votes_OT = 0

    #calculates total number of votes for each candidate using a for loop
    for row in csv_reader:
        Votes_T += 1
        if row[2] == "Khan":
            Votes_K += 1
        elif (row[2] == "Correy"):
            Votes_C += 1
        elif (row[2] == "Li"):
            Votes_Li += 1
        elif (row[2] == "O'Tooley"):
            Votes_OT += 1

#calculate each's candidate percentage
Percent_K = float("{0:.3f}".format(100 * Votes_K/Votes_T))
Percent_C = round(100 * Votes_C/Votes_T, 3)
Percent_Li = round(100 * Votes_Li/Votes_T, 3)
Percent_OT = round(100 * Votes_OT/Votes_T, 3)

#make a dictionary of candidates with their name and their percentage of votes
candidates = {  'Khan': Percent_K,
                'Correy': Percent_C, 
                'Li': Percent_Li, 
                'OTooley': Percent_OT }

#declare the winner of the vote
winner = max(candidates, key=candidates.get)

#print the results in the terminal
#create a separate text file with the results/analysis
with open("election_data.txt", "w") as text_file:
    print("Election Results", file = text_file)
    print("-------------------------", file = text_file)
    print("Total Votes: "+ str(Votes_T ), file = text_file)
    print("-------------------------", file = text_file)
    print("Khan: " +  str(Percent_K) +"%  (" + str(Votes_K )+ ")", file = text_file)
    print("Correy: " +  str(Percent_C) +"%  (" + str(Votes_C )+ ")", file = text_file)
    print("Li: " +  str(Percent_Li) + "%  (" + str(Votes_Li)+ ")", file = text_file)
    print("OTooley: " +  str(Percent_OT) +"%  (" + str(Votes_OT)+ ")", file = text_file)
    print("-------------------------", file = text_file)
    print("Winner: " + winner, file = text_file)
    print("-------------------------", file = text_file)

with open("election_data.txt", "r") as text_file:
    print(text_file.read())