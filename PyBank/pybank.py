#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Dependencies
import os
import csv

# file to load and output

file_to_load = os.path.join(".","Resources","budget_data.csv")
file_to_output = os.path.join(".","budget_analysis.txt")

total_months = 0
total = 0
net_change_list = []
all_rows = []

#read the csv and convert it into a list
with open(file_to_load) as financial_data:
    
    reader = csv.reader(financial_data, delimiter=",")
    
    #read the header row
    header = next(reader)
    first_row = next (reader)
    
    total_months = 1
    total = int(first_row[1])
    previous_net = int(first_row[1])

    for row in reader:
        all_rows.append(row)
        total_months += 1
        total += int(row[1])
        net_change = int(row[1])-previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        
average_change = sum(net_change_list) / len(net_change_list)
max_increase = max(net_change_list)
max_decrease = min(net_change_list)
max_increase_date = ""
max_decrease_date = ""  
    
for i, row in enumerate(all_rows):
        
# The greatest increase in profits (date and amount) over the entire period
    if net_change_list[i] == max_increase:
        max_increase_date = row[0]

# The greatest decrease in profits (date and amount) over the entire period
    if net_change_list[i] == max_decrease:
        max_decrease_date = row[0]

output =(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Month:{total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${round(average_change,2)}\n"
    f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")


with open(file_to_output,"w") as txt_file:
    txt_file.write(output)


# In[ ]:




