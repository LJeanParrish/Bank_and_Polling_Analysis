#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')

#Define lists and variables to store data
row_count = 0
Total_PNL = 0
Avg_Change = []
previous = 0
Max_Profit = ["", 0]
Min_Profit = ['', 999999999]
PNL_Diff = 0

print("Financial Analysis")
print("-------------------------")

#Part II - Loop through data set to print the calculations
# open csv file path

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
   
    # Read each row of data after the header
    csv_header = next(csvreader)        
    
    #Part III - Calculate the total number of months and add to row_count list
    for row in csvreader:    
        row_count = row_count + 1
        
        #Part IV - Calculate the changes in "Profit/Losses" over the entire period,
        Total_PNL = Total_PNL + int(row[1])
        PNL_Diff = int(row[1]) - previous

        #Add the differences to a list
        Avg_Change.append(PNL_Diff)
        previous = int(row[1])

        #Part V - The greatest increase in profits (date and amount) over the entire period

        if PNL_Diff > Max_Profit[1]:
            Max_Profit[1] = PNL_Diff 
            Max_Profit[0] = row[0]

         #PartVI - The greatest decrease in losses (date and amount) over the entire period

        if PNL_Diff < Min_Profit[1]:
            Min_Profit[1] = PNL_Diff 
            Min_Profit[0] = row[0]
    
    #Find the total average of PNL differences for the completed list
    Total_Avg = sum(Avg_Change[1:])/(len(Avg_Change)-1)
    Total_Avg =str(round(Total_Avg,2))

    # #Print all findings of Financial Analysis
    # print(f'Total Months: {row_count}')        
    # print(f'Total: ${Total_PNL}')
    # print(f'Average Change: ${Total_Avg}')
    # print(f'Greatest Increase in Profits: {Max_Profit[0]}, (${Max_Profit[1]})')
    # print(f'Greatest Decrease in Profits: {Min_Profit[0]}, (${Min_Profit[1]})')
    results = (f'Total Months: {row_count}\n'
    f'Total: ${Total_PNL}\n'
    f'Average Change: ${Total_Avg}\n'
    f'Greatest Increase in Profits: {Max_Profit[0]}, (${Max_Profit[1]})\n'
    f'Greatest Decrease in Profits: {Min_Profit[0]}, (${Min_Profit[1]})')
    print(results)
#Part VII - specify the file export the Financial Data to write as txt file)
# Set variable for output file
output_file = os.path.join('..', 'Pybank', 'Analysis',"Financial_Analysis.txt")

# Open the output file
with open(output_file, "w", newline="") as txtfile:
    # writer.writerow(["Financial Analysis"])
    # writer.write([f'Total Months: {row_count}\n'])
    # writer.writerow(["Total: $38382578"])
    # writer.writerow(["Average Change: $-2315.12"])
    # writer.writerow(["Greatest Increase in Profits: Feb-2012, ($1926159)"])
    # writer.writerow(["Greatest Decrease in Profits: Sep-2013, ($-2196167)"])

    txtfile.write(results)
   