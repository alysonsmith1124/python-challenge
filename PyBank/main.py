import os
import csv

#Define file path
input_path = os.path.join("..","..","WUSTL201904DATA2","02-Homework","03-Python","Instructions","PyBank","Resources","budget_data.csv")
output_path = "pybank.txt"

#Set variables
Month_Total = 0
Net_Total = 0
Net_Change = 0
Net_Change_List = []
    
#Open and read csv file
with open(input_path, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #Pull out first row values to make net change easier
    First_Row = next(csvreader)
    Month_Total = Month_Total + 1
    Net_Total = Net_Total + int(First_Row[1])
    Prev_Row = int(First_Row[1])
    Greatest_Increase = ["",0]
    Greatest_Decrease = ["", 999999999999999]

    for row in csvreader:
        #Iterate through rows and total the number of months and total profit/loss
        Month_Total = Month_Total + 1
        Net_Total = Net_Total + int(row[1]) 
        
        #Iterate through rows and find the net change and add to list
        Net_Change = int(row[1])-Prev_Row
        Prev_Row = int(row[1])
        Net_Change_List.append(Net_Change)
 
        #Find the greatest net change increase
        if Net_Change > Greatest_Increase[1]:
            Greatest_Increase[0] = row[0]
            Greatest_Increase[1] = Net_Change
        
        #Find the greatest net change decrease
        if Net_Change < Greatest_Decrease[1]:
            Greatest_Decrease[0] = row[0]
            Greatest_Decrease[1] = Net_Change

    #Find the average of the net changes over entire period
    Average_Change = sum(Net_Change_List) / len(Net_Change_List)


    output = (
    "Financial Analysis\n"
    "----------------------\n"
    f"Total Months: {Month_Total}\n"
    f"Total: ${Net_Total}\n"
    f"Average Change: ${Average_Change:.2f}\n"
    f"Greatest Increase in Profits: {Greatest_Increase[0]} (${Greatest_Increase[1]})\n"
    f"Greatest Decrease in Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})")

    print(output)

    with open(output_path, 'w', newline='') as txt_output:
        txt_output.write(output)