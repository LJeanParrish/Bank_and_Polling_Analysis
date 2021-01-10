#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

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

        #Find the average of the PNL differences
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

    Total_Avg = sum(Avg_Change[1:])/(len(Avg_Change)-1)

    print(f'Total Months: {row_count}')        
    print(f'Total: ${Total_PNL}')
    print(f'Average {Total_Avg}')
    print(Max_Profit[0], Max_Profit[1])
    print(Min_Profit[0], Min_Profit[1])



    # row=2
    # row_count = 0+1 =1
    # total_pnl = 0 + 867884
    # PNL_Diff = 867884- 0 = 867884
    # Avg_Change = [867884]
    # previous = 867884


    # row = 3
    # row_count = 1+1 =2
    # total_pnl =867884 + 967880 = 15000000
    # PNL_Diff = 967880 - 867884 =xyz
    # Avg_Change = [867884, xyz]
    # previous = 967880

    #   row = 4
    # row_count =2+1 +3
    # total_pnl =15000000 + int(row[1])
    # PNL_Diff = 322013-967880 = -abc
    # Avg_Change = [867884,xyz,-abc]
    # previous = 322013


#Part VII - specify the file export the Financial Data to write as txt file)
# Set variable for output file
# output_file = os.path.join("Financial_Analysis.csv")

# Open the output file
# with open(output_file, "w", newline="") as datafile:
# #     writer = csv.writer(datafile)
