#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Define lists to store data
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Total_PNL = 0
Max_Profit = 0
Min_Profit = 0
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
        row_count = sum(1 for row in csvreader)
        print(f'Total Months: {1 + row_count}')
        print(row[1])  #test code

        #Part III - Total the net amount of profits and losses
        #Loop through row[1] and add all data points and print total
        Total_PNL = sum(range(int(row[1])))
        print(f'Total: ${Total_PNL}')
        
        #Option1
        #for i in range(len(Total_PNL)):
            #print(f'(Total: {sum([float(i) for i in csvreader])})')        

        #Option2
        #Total_PNL = [row[-1] for row in csvreader]
        #sum([float(i) for i in range(len(Total_PNL))])
        #print(Total_PNL)

        #Option3
        #Total_PNL = [row[-1] for row in csvreader]
        #print(f'Total: {sum([float(i) for i in range(len(Total_PNL))])}')        
        
        #Option4      
        #Total_PNL = sum(float(row[1]) for row in csvreader)
        #print(f'Total: {Total_PNL}')


        
        
        #Part IV - Calculate the changes in "Profit/Losses" over the entire period,
        #Max_Profit = max(row[1])
        #Min_Profit = min(row[1])

        #PNL_Diff = (Max_Profit - Min_Profit)

        # Then find the average of those changes

        #Avg_Change = (PNL_Diff / (1 + row_count))

        #print(f'Average Change ${Avg_Change}')


        


#Part V - The greatest increase in profits (date and amount) over the entire period
#PartVI - The greatest decrease in losses (date and amount) over the entire period

#Part VII - specify the file export the Financial Data to write as txt file)
# Set variable for output file
# output_file = os.path.join("Financial_Analysis.csv")

# #  Open the output file
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)
