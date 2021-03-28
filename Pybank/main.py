#import libraries
import os
import csv
#create path
csv_path = os.path.join('budget_data.csv')
#define change as a dictionary 
changes = {}
#read csv file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #store csv header
    csv_header = next(csv_reader)
    #turn csv into list 
    csv_list = list(csv_reader)
    #count months
    amount_of_months = len(csv_list)
    total_profit = 0
    #identify columns
    for row in range(0, amount_of_months):
        month = csv_list[row][0]
        profit_loss = int(csv_list[row][1])
        #accumluate total net profit
        total_profit += int(profit_loss)
        
        if row != len(csv_list) - 1:
            #define key (month) 
            key = csv_list[row + 1][0]
            #record difference into changes dictionary 
            changes[key] = int(csv_list[row + 1][1]) - int(profit_loss)
    #grab values from dict. and put into list
    profit_changes = changes.values()
    #define average changeund(sum(profit_changes
    average_change = str(round(sum(profit_changes)/len(profit_changes), 2))
    #define greatest increase month
    greatest_increase_month = max(changes, key=changes.get)
    #define greatest decrease month
    greatest_descrease_month = min(changes, key=changes.get)
    #define greatest increase
    greatest_increase = changes[greatest_increase_month]
    #define greatest decrease
    greatest_descrease = changes[greatest_descrease_month]
    #print analysis
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f'Total Months: {amount_of_months}')
    print(f'Total Profits: ${total_profit}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_descrease_month} (${greatest_descrease})')

with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------------------------------------\n")
    text.write(f'Total Months: {amount_of_months}\n')
    text.write(f'Total Profits: ${total_profit}\n')
    text.write(f'Average Change: ${average_change}\n')
    text.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    text.write(f'Greatest Decrease in Profits: {greatest_descrease_month} (${greatest_descrease})\n')


        
        
    
        
   

        

    

  

        
    