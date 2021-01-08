#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Define lists to store data
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Total_Month = []

print("Financial Analysis")
print("-------------------------")

#Part II - Loop through the data set to print the calculations
# open csv file path

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
   
    csv_header = next(csvreader)
        
    # Read each row of data after the header
    for row in csvreader:
        row_count = sum(1 for row in csvreader)
        #total_months = row[0]
        #total_months += 1
        print(f'Total Months: {1 + row_count}')
        #Total_Month = row[0]
        #print(f'Total Months  + {range(len(Total_Month))}')
        #print(row[0])
        #if row[0] == month
        #Calculate the total number of months and add to Total_month list
        #Total_Month.append(Total_Month[int(month)])        
        #print(row)
        #print(month.index(month))
        #for month in range(len(total_month)):
        #print(total_month.index(month))
        #print("[" + str(month) + "] " + total_month[month])
    
#Part III - Total the net amount of profits and losses
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
