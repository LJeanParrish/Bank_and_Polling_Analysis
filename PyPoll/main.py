#Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Define lists and variables to store data
row_count = 0
canidate_list = []

print("Election Results")
print("-------------------------")

#Retrieve data from CSV file path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
      
    # Read each row of data after the header
    csv_header = next(csvreader)  

    #create canidate dictionary to store election results
    canidatedict = {}    

    for row in csvreader:

        #Calculate the total number of individual votes in the election
        row_count = row_count + 1 

        #Loop through data set and add canidates to canidate list      
        if row[2] not in canidate_list:
            canidate_list.append(row[2])
            canidatedict[row[2]] = 0

        #Add the number of votes each canidate received 
        canidatedict[row[2]] = canidatedict[row[2]] + 1
    
    #print election results
    print(f'Total Votes: {row_count}')    
    print("-------------------------")
      
    canidateperdict = {} 
    maxcount = 0

    for canidate in canidatedict:
        canidateperdict[canidate] = round((canidatedict[canidate]/row_count * 100), 3)         
        print(f'{canidate}: {canidateperdict[canidate]}% ({canidatedict[canidate]})')

        #Determine which canidate is the winner
        if canidatedict[canidate] > maxcount:
            maxcount = canidatedict[canidate]
            winner = canidate 
    
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")   

    Election_Final = (f'Total Votes: {row_count}\n'
    f'{canidate}: {canidateperdict[canidate]}% ({canidatedict[canidate]})\n'
    f'Winner: {winner}')
   
#Specify the file export for the election results to write as txt file)
#Set variable for output file
output_file = os.path.join('..', 'Pypoll', 'Analysis',"Election_Results.txt")

# Open the output file
with open(output_file, "w", newline="") as txtfile:
    txtfile.write(Election_Final)
    
   