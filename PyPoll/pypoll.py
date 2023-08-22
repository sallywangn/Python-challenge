#!/usr/bin/env python
# coding: utf-8

# In[32]:


import os
import csv

file_to_load = os.path.join(".","Resources","election_data.csv")
file_to_output = os.path.join(".","election_analysis.txt")


total_votes = 0

candidate_vote ={}
candidate_options =[]
candidate_percentages ={}
winning_count = 0
winning_candidate =""

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    header = next(reader)

# The total number of votes cast
    
    for row in reader:
        total_votes = total_votes+1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_vote[candidate_name] =0
        candidate_vote[candidate_name]+=1

election_results=(f"Election Results: \n"
       f"-------------------------\n"
       f"Total Votes: {total_votes}\n"
       f"-------------------------\n")
print(election_results, end="")

with open(file_to_output, "w") as txt_file:
    txt_file.write(election_results)
        
    for candidate in candidate_vote:
        votes = candidate_vote[candidate]
        percentage =(candidate_vote[candidate]/total_votes)*100
        percentage_string =f"{percentage:.3f}%"
        candidate_percentages[candidate]=percentage_string
 
        voter_output = f"{candidate}: {percentage_string} ({votes})\n"
        print(voter_output, end="")
    
        txt_file.write(voter_output)
    
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
    
    winning_result=(f"-------------------------\n"
                    f"Winner: {winning_candidate}\n"
                    f"-------------------------\n")
    print(winning_result)
    
    txt_file.write(winning_result)


# In[ ]:




