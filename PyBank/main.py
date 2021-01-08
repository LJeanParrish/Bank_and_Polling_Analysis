#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Define lists to store data
#month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
row_count = 0
pnl = []
Total_PNL = 0
Avg_Change = []
previous = 0
Max_Profit = ["", 0]
Min_Profit = ['', 999999999]
PNL_Diff = 0

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
        print(row)
        row_count = row_count + 1
        #row_count = sum(1 for row in csvreader)


        Total_PNL = Total_PNL + int(row[1])
        PNL_Diff = int(row[1]) - previous
        Avg_Change.append(PNL_Diff)
        previous = int(row[1])

        if PNL_Diff > Max_Profit[1]:
            Max_Profit[1] = PNL_Diff 
            Max_Profit[0] = row[0]

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





        
#         print(row[1]) #test code  

#         #Part III - Total the net amount of profits and losses
#         #Loop through row[1] and add all data points and print total
#         #Option 10
#         Total_PNL = sum(pnl for row[1] in csvreader)
#         print(f'Total: ${Total_PNL}')

#         #Option 6      
#         #Total_PNL = sum(range(int(row[1])))
#         #print(f'Total: ${Total_PNL}')
        
                
#         #Option 9    
#         #Total_PNL = sum(range(row[1]) for pnl in csvreader)
#         #print(f'Total: ${Total_PNL}')

        
#         #Option 8
#         #csv_header = csv.reader(open(csvpath))
#         #csv_header = next(csvreader) 
#         #print(sum(int(x[1]) for x in csv_header))

#         #option 7
#         #reader = csv.DictReader(csvfile)
#         #Total_PNL = sum(float(row[1]) for row in reader)
#         #print(f'Total: ${Total_PNL}')

#         #Option 6      
#         #Total_PNL = sum(range(int(row[1])))
#         #print(f'Total: ${Total_PNL}')
        
#         #Option1
#         #for i in range(len(Total_PNL)):
#             #print(f'(Total: {sum([float(i) for i in csvreader])})')        

#         #Option2
#         #Total_PNL = [row[-1] for row in csvreader]
#         #sum([float(i) for i in range(len(Total_PNL))])
#         #print(Total_PNL)

#         #Option3
#         #Total_PNL = [row[-1] for row in csvreader]
#         #print(f'Total: {sum([float(i) for i in range(len(Total_PNL))])}')        
        
#         #Option4      
#         #Total_PNL = sum(float(row[1]) for row in csvreader)
#         #print(f'Total: {Total_PNL}')
        
        
#         #Part IV - Calculate the changes in "Profit/Losses" over the entire period,
#         #Max_Profit = max(row[1])
#         #Min_Profit = min(row[1])

#         #PNL_Diff = (Max_Profit - Min_Profit)

#         # Then find the average of those changes

#         #Avg_Change = (PNL_Diff / (1 + row_count))

#         #print(f'Average Change ${Avg_Change}')
        


#         #Part V - The greatest increase in profits (date and amount) over the entire period
#         #Use Max_Profit calculated in part III to bring back corresponding date

#         #print(f'Greatest Increase in Profits: Date ${(Max_Profit)}')
        
#         #PartVI - The greatest decrease in losses (date and amount) over the entire period
#         #Use Min_Profit calculated in part III to bring back corresponding date

#         #print(f'Greatest Increase in Profits: Date ${(Min_Profit)}')


# #Part VII - specify the file export the Financial Data to write as txt file)
# # Set variable for output file
# # output_file = os.path.join("Financial_Analysis.csv")

# # #  Open the output file
# # with open(output_file, "w", newline="") as datafile:
# #     writer = csv.writer(datafile)
