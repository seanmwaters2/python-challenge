#import libraries
import os
import csv
#create path
csv_path = os.path.join('election_data.csv')
#dictionary containing voting data
voting_data = {}
#open and read file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #store header
    csv_header = next(csv_reader)
    #made list for csv file
    csv_list = list(csv_reader)
    #count amount of votes
    amount_of_votes = len(csv_list)
    #loop through each row
    for row in csv_list:
        #if name is not in our dictionary then count 1          .keys grabs list of keys (unique names) 
        if row[2] not in voting_data.keys():
            voting_data[row[2]] = 1
        #else if we've seen name before add 1 to total
        else:
            voting_data[row[2]] += 1
    #print analysis
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {amount_of_votes}')
    print('-------------------------')
    #add total votes of each candidate and adds them together
    total = sum(list(voting_data.values()))
    #loop through each key in our dictionary 
    for candidate in voting_data:
        #grabbing value (votes) of key (candidates)
        votes = voting_data[candidate]
        #calculating percentage and formating to add % sign
        vote_percentage = "{:.3%}".format(((voting_data[candidate])/int(total)))
        #print keys (candidates) and values
        print(f'{candidate}: {vote_percentage} ({votes})')
    #use max function to get winner
    winner = max(voting_data, key=voting_data.get)
    #print anaylsis
    print('-------------------------')
    print(f'Total Winner: {winner}')
    print('-------------------------')

with open('election_results.txt', 'w') as text:
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write(f'Total Votes: {amount_of_votes}\n')
    text.write('-------------------------\n')
    for candidate in voting_data:
        votes = voting_data[candidate]
        vote_percentage = "{:.3%}".format(((voting_data[candidate])/int(total)))
        text.write(f'{candidate}: {vote_percentage} ({votes})\n')
    text.write('-------------------------\n')
    text.write(f'Total Winner: {winner}\n')
    text.write('-------------------------\n')