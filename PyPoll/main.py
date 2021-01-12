#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Define lists and variables to store data
row_count = 0
canidate_list = []

print("Election Results")
print("-------------------------")

#Part II - Retrieve data from CSV file path
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
        #Add the number of votes each canidate received
        
        if row[2] not in canidate_list:
            canidate_list.append(row[2])
            canidatedict[row[2]] = 0

        canidatedict[row[2]] = canidatedict[row[2]] + 1
    
    print(f'Total Votes: {row_count}')    
    print("-------------------------")
    print(canidate_list)    
    print(canidatedict)
#         #Capture the canidate list
#         #Calculate the total of votes each canidate won
    canidateperdict = {} 
    maxcount = 0
    for canidate in canidatedict:
        canidateperdict[canidate] = round((canidatedict[canidate]/row_count * 100), 2)
        #print(canidate)
        print(f'{canidate}, {canidateperdict[canidate]}%, {canidatedict[canidate]}')

        if canidatedict[canidate] > maxcount:
            maxcount = canidatedict[canidate]
            winner = canidate
    print(winner)



#         khan_count = 
#         correy_count =
#         li_count =
#         otooley_count = 
    
       

#         #Calculate the percentage of votes each candidate won
#         kpercent = (khan_count)/(row_count)
#         kpercent =str(round(kpercent,2))

#         cpercent = (correy_count)/(row_count)
#         cpercent =str(round(cpercent,2))

#         lpercent = (li_count)/(row_count)
#         lpercent =str(round(cpercent,2))

#         opercent = (otooley_count)/(row_count)
#         opercent =str(round(cpercent,2))


# #Create a dictionary which holds all election results
# election_results = {['canidate': "Khan", 'percent': kperent, 'vote': khan_count],
# ['canidate': "Correy", 'percent': cperent, 'vote' : correy_count],
# ['canidate': "Li", 'percent': lperent, 'vote': li_count],
# ['canidate': "O'Tooley", 'percent': operent, 'vote': otooley_count]}

# #Print all analysis on Election Results
# print(f'Total Votes: {1 + row_count}')
# print("-------------------------")
# print(election_results)      


# #The winner of the election based on popular vote
# #Create conditional to determine election results
# If khan_count > correy_count and li_count, and otooley_count:
# print("Winner: Khan")

# If correy_count > khan_count and li_count and otooley_count:
# print("Winner: Correy")

# If li_count > khan_count and correy_count and otooley_count:
# print("Winner: Li")

# If otooley_count  > khan_count and correy_count and li_count:
# print("Winner: O'Tooley")

    
#     ###Other Attempts for part 2--------------------------------------------------
#     #     if str(row[2]) == Khan:
#     #         Khan_Vote.append(khan)
#     # print(Khan_Vote)

#     #option 4
#      # khan_vote = khan_vote + int(row[2])
#         # khan_count = int(row[2]) - previous
#         # khan_total.append(khan_count)
#         # previous = int(row[2])

#     #option 5
#         #Create a list which will store canidate names
#         #  if canidate == Khanint([2]:
#         #     khan_count = Khan + 1
            
#         # if canidate == Correy[2]:
#         #     correy_count == Correy + 1

#         # if canidate == Li[2]:
#         #     li_count = Li + 1

#         # if canidate == OTooley[2]:
#         #     otooley_count = "O'Tooley" + 1          
            

#             # canidate_list.append(canidate)
#             # previous = int(row[2])   
        
#         # #option 3
#         # if canidate not in canidate_list:
#         #     canidate_list.append(canidate)
#         #     previous = str(row[2])
        
#         # #Option 2
#         # canidate = canidate + str(row[2])
#         # canidate_count = str(row[2]) - previous
#         # canidate_list.append(canidate_count)
#         # previous = str(row[2])
        
        
#         # #Option 1
#         # #if (row[2]) not in canidate_list:
#         #     #canidate_list.append(row[2])
#         #     # #previous = row[2]
        



# #Specify the file export the Financial Data to write as txt file)
# # Set variable for output file
# #output_file = os.path.join('..', 'Pypoll', 'Analysis',"Election_Results.csv")

# # Open the output file
# # with open(output_file, "w", newline="") as csvfile:
# #     writer = csv.writer(csvfile)
# #     writer.writerow(["Election Results"])
# #     writer.writerow(["Total Votes: "])
# #     writer.writerow([""])
# #     writer.writerow([""])
# #     writer.writerow([""])
# #     writer.writerow([""])
   