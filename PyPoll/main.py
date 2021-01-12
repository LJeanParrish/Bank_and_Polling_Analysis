#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Define lists and variables to store data
row_count = 0
total_canidate = ""
canidate_list = []
previous = ""
#canidate_count = ""
Khan_Vote = 0
Khan = ""

print("Election Results")
print("-------------------------")

#Part II - Loop through the data set to print the calculations
# open csv file path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
   
    # Read each row of data after the header
    csv_header = next(csvreader)        
    
    #Calculate the total number of individual votes and add to row_count list
    total_canidate = total_canidate + str(row[2])
    canidate_count = str(row[2]) - previous

    #Add canidates to a list
    canidate_list.append(canidate_count)
    previous = str(row[2])
    
    
    
    
    
    # for row in csvreader:
    #     row_count = sum(1 for row in csvreader)

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
   