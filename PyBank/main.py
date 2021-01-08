#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Define lists to store data
#month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Total_PNL = []

print("Financial Analysis")
print("-------------------------")

#Part II - Loop through the data set to print the calculations
# open csv file path

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
   
    # Read each row of data after the header
    csv_header = next(csvreader)        
    
    #Calculate the total number of months and add to row_count list
    for row in csvreader:
        row_count = sum(1 for row in csvreader)
        print(f'Total Months: {1 + row_count}')
        print(row[1:])  #test code

        #Part III - Total the net amount of profits and losses
        #Loop through row[1] and add all data points and print total
        
        
        
        
        Total_PNL = sum(float(row[1]) for row in csvreader)
        print(f'Total: {Total_PNL}')        
        
        
        #Part IV - Calculate the changes in "Profit/Losses" over the entire period,














# Then find the average of those changes
#Part V - The greatest increase in profits (date and amount) over the entire period
#PartVI - The greatest decrease in losses (date and amount) over the entire period

#Part VII - specify the file export the Financial Data to write as txt file)
# Set variable for output file
# output_file = os.path.join("Financial_Analysis.csv")

# #  Open the output file
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)
