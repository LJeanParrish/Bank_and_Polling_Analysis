Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data')

#Define lists to store data


print("Election Results")
print("-------------------------")

#Part II - Loop through the data set to print the calculations
# open csv file path

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
   
    # Read each row of data after the header
    csv_header = next(csvreader)        
    
    #Calculate the total number of votes and add to row_count list
    for row in csvreader:
        #row_count = sum(1 for row in csvreader)
        #print(f'Total Votes: {1 + row_count}')