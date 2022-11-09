# import the required modules
import os
import csv

# Create a path for the file
election_data_path = os.path.join('..', 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')


def sum(arry):
    _sum = 0

    for i in arry:
        _sum = _sum + i
    
    return(_sum)

def mean(arr):
    mean_ = sum(arr)/len(arr)

    return(mean_)

votes = []

with open(election_data_path) as election_csv:
    csv_election_data = csv.reader(election_csv, delimiter = ',')

    budget_header = next(csv_election_data)

    for row in csv_election_data:
        # print(row)
        votes.append(row[2])
    # print(votes)

total_votes = len(votes)
candidate = []
for vote in votes:
    if vote not in candidate:
        candidate.append(str(vote))

print(total_votes)
