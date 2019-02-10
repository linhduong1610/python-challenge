print("Financial Analysis")
print("--------------------------")
import os 
import csv 

total_months = []
change_revenue = []
revenue = []
average_change = []   
total_change = []


csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r', newline='') as budget: 
    csvreader = csv.reader(budget, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        total_months.append(row[0])
        revenue.append(int(row[1]))        
   
    for i in range(len(revenue)-1):
        change_revenue.append(revenue[i+1] - revenue[i])
 
average_change = (sum(change_revenue))/len(change_revenue)
max_increase = max(change_revenue)
max_decrease = min(change_revenue)

max_month = change_revenue.index(max_increase) + 1
min_month = change_revenue.index(max_decrease) + 1

print(f'Total Months: {len(total_months)}')
print(f'Total: $ {sum(revenue)}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {total_months[max_month]} (${(str(max_increase))})')
print(f'Greatest Decrease in Profits: {total_months[min_month]} (${(str(max_decrease))})')

file = open('Summary.txt','w')
file.write('Financial Analysis' + '\n')
file.write('...............................' + '\n')
file.write(f'Total Months: {len(total_months)}'+ '\n')
file.write(f'Total: $ {sum(revenue)}'+ '\n')
file.write(f'Average Change: ${round(average_change,2)}'+ '\n')
file.write(f'Greatest Increase in Profits: {total_months[max_month]} (${(str(max_increase))})'+ '\n')
file.write(f'Greatest Decrease in Profits: {total_months[min_month]} (${(str(max_decrease))})'+ '\n')
   