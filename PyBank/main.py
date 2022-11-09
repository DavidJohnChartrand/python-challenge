# import the required modules
import os
import csv

# Create a function that with count the number of rows 
#this is the same as counting the months


# Create a path for the file
budget_data_path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# define a formula to count the number of rows
# this will be the same as counting the number of months

def sum(arry):
    _sum = 0

    for i in arry:
        _sum = _sum + i
    
    return(_sum)

def mean(arr):
    mean_ = sum(arr)/len(arr)

    return(mean_)

def Diff_array(arra):
    dif=[]
    for i in range(len(arra)-1):
        dif.append(arra[i+1] - arra[i])
    return dif

Profit_list = []
Date_list=[]

with open(budget_data_path) as budget_csv:

    csv_budget_data = csv.reader(budget_csv, delimiter=',')

    # remove the header
    budget_header = next(csv_budget_data)
    # print(budget_header)
    for row in csv_budget_data:
        
        Profit_list.append(float(row[1]))
        Date_list.append(row[0])
    
        # print(float(row[1]))

TotalProfit = sum(Profit_list)
Profit_diff = Diff_array(Profit_list)

Mean_profit_change = mean(Profit_diff)

ChangesInProfit = []


# print(month_count)

print(len(Profit_list))
print(TotalProfit)
print(Mean_profit_change)
print(max(Profit_diff))
print(min(Profit_diff))
max_mon = (Profit_diff.index(max(Profit_diff)))+1
min_mon = (Profit_diff.index(min(Profit_diff)))+1
print(Date_list[max_mon])
print(Date_list[min_mon])