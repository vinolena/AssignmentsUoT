import csv
from collections import Counter

# initialize variables
votes = 0
candidate_list = []

# open and read csv file
with open("/Users/elenavinyukova/Desktop/AssignmentsUoT/PyPoll/Resources/election_data.csv", "r") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    # skip the header row
    next(election_data)
    # iterate through rows
    for row in election_data:
        # increment the number of votes
        votes += 1
        # add candidate to list
        candidate_list.append(row[2])

# count the number of votes for each candidate
candidate_votes = Counter(candidate_list)

# print the results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {votes}")
print("----------------------------")

# iterate through candidates and their votes
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes/sum(candidate_votes.values()):.3%} ({votes})")
print("----------------------------")

# find the winner of the election
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("----------------------------")

#export results to a text file
with open("election_results.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Votes: {votes}\n")
    text_file.write("----------------------------\n")
    for candidate, votes in candidate_votes.items():
        text_file.write(f"{candidate}: {votes/sum(candidate_votes.values()):.3%} ({votes})\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("----------------------------\n")