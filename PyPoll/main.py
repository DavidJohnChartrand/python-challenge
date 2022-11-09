# import the required modules
import os
import csv

# Create a path for the file
election_data_path = os.path.join('..', 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')
analysis_path = os.path.join('..', 'python-challenge', 'PyPoll', 'analysis', 'analysis.txt')


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
candidate_votes = []
for vote in votes:
    if vote not in candidate:
        candidate.append(str(vote))
        candidate_votes.append(0)
    for candi in candidate:
        if vote == candi:
            candidate_votes[candidate.index(candi)] +=1
            # print(candi)

print(f'Election Results')
print(f'----------------------------------------')
print(f'Total Votes: {total_votes}')
print(f'----------------------------------------')
most_votes = 0
for great_v in candidate_votes:
    if great_v > most_votes:
        most_votes = great_v
# Created a for loop to print out the candidate and they percentatage of the total vote so that this code is more reuseable
# As the number of candidate might vary from election to election
for candi in range(len(candidate)):
    print(f'{candidate[candi]}: {round((candidate_votes[candi]/total_votes)*100, 3)}% ({candidate_votes[candi]})')

print(f'----------------------------------------')

# print(candidate_votes.index(most_votes))
print(f'Winner: {candidate[(candidate_votes.index(most_votes))]}')
print(f'----------------------------------------')

with open(analysis_path,'w') as analysis:
    print(f'Election Results', file=analysis)
    print(f'----------------------------------------', file=analysis)
    print(f'Total Votes: {total_votes}', file=analysis)
    print(f'----------------------------------------', file=analysis)
    for candi in range(len(candidate)):
        print(f'{candidate[candi]}: {round((candidate_votes[candi]/total_votes)*100, 3)}% ({candidate_votes[candi]})', file=analysis)\
    
    print(f'----------------------------------------', file=analysis)
    print(f'Winner: {candidate[(candidate_votes.index(most_votes))]}', file=analysis)
    print(f'----------------------------------------', file=analysis)
