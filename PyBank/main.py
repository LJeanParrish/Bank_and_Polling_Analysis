#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Define lists to store data
month = ["Jan-", "Feb-", "Mar-", "Apr-", "May-", "Jun-", "Jul-", "Aug-", "Sep-", "Oct-", "Nov-", "Dec-"]
total_month = []

print("Financial Analysis")
print("-------------------------")

#Part II - Identify the total number of months included in the data set
# open csv file path

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        #print(month.index(month))

        # Loop through months and add to total_month list
        #for month in range(len(total_month)):
            #print(total_month.index(month))
            
            
            #print("[" + str(month) + "] " + total_month[month])
    
#Part III - Total the net amount of profits and losses
#Part IV - Calculate the changes in "Profit/Losses" over the entire period,
# Then find the average of those changes
#Part V - The greatest increase in profits (date and amount) over the entire period
#PartVI - The greatest decrease in losses (date and amount) over the entire period

#Part VII - specify the file export the Financial Data to write as txt file
# output_path = os.path.join("..", "Analysis", "Fin_Analysis.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])