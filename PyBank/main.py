#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Define lists to store data
month = 0
total_month = []

#open csv file path

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)


#Part II - Identify the total number of months included in the data set
        # Loop through months and add to total_month list
        #for month in range(len(total_month)):
            #print(total_month.index(month))
            
            
            #print("[" + str(month) + "] " + total_month[month])
    
        






















# Specify the file export the Financial Data to write as txt file
# output_path = os.path.join("..", "Analysis", "Fin_Analysis.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])