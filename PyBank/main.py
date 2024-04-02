#MODULE 3 CHALLENGE

import os
import csv

#initalize variable for calculation for the months
months=0
#initalize variable for calculation for the net total amount of profit/losses
netTotal=0
#initialize variables for calculation for the changes in "Profit/Losses" over the entire period
#and the average
currentMonth=0
previousMonth=0
#store the changes in a list to be able to calculate the average
changeList= []
#initalize variables for the greatest increase and greatest decrease in profits
greatestInc=0
greatestDec=0

budget_data = os.path.join('Resources/budget_data.csv')
results=os.path.join('Analysis/results.txt')
#open and read csvfile
with open(budget_data) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader= csv.reader(csvfile,delimiter=",")
    #skip first row
    next(csvreader)
   
    #read each row of data after the header
    for row in csvreader:
        #calculate total months
        months +=1
        #calculate net total
        netTotal += int(row[1])
        #get the value of the current month
        currentMonth = int(row[1])
       
        #after the first month, you can start calculating the change per month
        if months > 1:
            change= currentMonth-previousMonth
            #add the change to be stored in the list
            changeList.append(change)
            
            #find the greatest increase in profit
            if change>greatestInc:
                greatestInc=change
                #get the date
                gidate= row[0]
            #find the greatest decrease in profit
            if change<greatestDec:
                greatestDec=change
                #get the date
                gddate=row[0]
        #once the change has been calculated, move on to the next month
        num_changes= months-1
        previousMonth=currentMonth
        
    #calculate the average change per month, and round 2 decimal places
    avgChange= round(sum(changeList)/ num_changes, 2)

#print AND export the table
#create list to export
#PRINT RESULTS
output= (
    "Financial Analysis\n"
    "--------------------------------\n"
    f"Total months: {months}\n"
    f"Total: $ {netTotal}\n"
    f"Average Change: $ {avgChange}\n"
    f"Greatest Increase in Profits: {gidate} (${greatestInc})\n"
    f"Greatest Decrease in Profits: {gddate} (${greatestDec})\n")
#print to terminal
print(output)
#print results to a text file
with open(results, 'w') as txt_file:
    txt_file.write(output)






