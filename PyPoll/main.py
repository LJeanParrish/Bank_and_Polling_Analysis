#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Define lists and variables to store data
row_count = 0
total_canidate = ""
canidate_list = []
previous = 0
canidate_count = ""

khan_vote = 0
khan_count = 0
khan_total = []
correy_vote = 0
li_vote = 0
otooley_vote = 0



print("Election Results")
print("-------------------------")

#Part II - Loop through the data set to print the calculations
# open csv file path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
   
    # Read each row of data after the header
    csv_header = next(csvreader)       

    for row in csvreader:

        #Calculate the total number of individual votes and add to row_count list
        row_count = sum(1 for row in csvreader) 
        
        #Capture the canidate list
        for canidate in csvreader:
            canidate = canidate + str(row[2])
            canidate_list.append(canidate)
            previous = int(row[2])

        #The percentage of votes each candidate won


        #The total number of votes each candidate won
        # khan_vote = khan_vote + int(row[2])
        # khan_count = int(row[2]) - previous
        # khan_total.append(khan_count)
        # previous = int(row[2])


        #The winner of the election based on popular vote
        #if then statement


    
    ###Other Attempts for part 2--------------------------------------------------
    #     if str(row[2]) == Khan:
    #         Khan_Vote.append(khan)
    # print(Khan_Vote)



        #Create a list which will store canidate names
        # canidate = canidate + str(row[2])
        
        # #option 3
        # if canidate not in canidate_list:
        #     canidate_list.append(canidate)
        #     previous = str(row[2])
        
        # #Option 2
        # canidate = canidate + str(row[2])
        # canidate_count = str(row[2]) - previous
        # canidate_list.append(canidate_count)
        # previous = str(row[2])
        
        
        # #Option 1
        # #if (row[2]) not in canidate_list:
        #     #canidate_list.append(row[2])
        #     # #previous = row[2]
        
#Print all analysis on Election Results
print(f'Total Votes: {1 + row_count}')
print("-------------------------")
print(canidate_list)

#Specify the file export the Financial Data to write as txt file)
# Set variable for output file
output_file = os.path.join('..', 'Pypoll', 'Analysis',"Election_Results.csv")

# Open the output file
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Election Results"])
    writer.writerow([""])
    writer.writerow([""])
    writer.writerow([""])
    writer.writerow([""])
    writer.writerow([""])
   