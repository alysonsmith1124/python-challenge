import os
import csv

#Define file path
budget_csv = os.path.join("..","..","WUSTL201904DATA2","02-Homework","03-Python","Instructions","PyBank","Resources","budget_data.csv")

#Set variables
Month_Total = 0
Net_Total = 0

#Define Function
def average(num1,num2):
    


#Open and read csv file
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #loop through each row in data
    for row in csvreader:
        Month_Total = Month_Total + 1
        Net_Total = Net_Total + int(row[1]) 

    print(Net_Total)

