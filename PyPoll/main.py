print("Election Result")
print("-------------------------------")
import os
import csv


csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath, 'r', newline='') as election:
    csvreader = csv.reader(election, delimiter=',')
    next(csvreader)
    
    total_candidates = []
    total_votes = 0
    voter = []
    candidates = []
    percent_vote = []
    final_result =[]
    

    for row in csvreader:
        total_candidates.append(row[2])
        total_votes += 1 
    
    print(f'Total Votes: {total_votes}')
    print("-------------------------------")
    
    sorted_candidate = sorted(total_candidates)

    for i in range(total_votes):
        if sorted_candidate[i-1] != sorted_candidate[i]:
            candidates.append(sorted_candidate[i])
    for j in range(len(candidates)):
        vote_count = 0 

        for k in range(len(sorted_candidate)):
            if candidates[j] == sorted_candidate[k]:
                vote_count += 1
        voter.append(vote_count)
        percent_vote.append(round((vote_count/total_votes)*100,3))
    
    zip_data = zip(candidates, percent_vote, voter)
    for row in zip_data:
        print(row[0] + ":", str(row[1]) +"%"+ " (" +str(row[2]) +")")
        result = (row[0] + ":", str(row[1]) +"%"+ " (" +str(row[2]) +")")  
        final_result.append(result)

    print("-------------------------------")         

    for h in range(len(percent_vote)):
        if voter[h] > voter[h-1]:
            winning_candidate = candidates[h]

    print(f'Winner: {winning_candidate}')
    print("-------------------------------")  

output_path = os.path.join("Election_Result")
with open(output_path, 'w', newline='') as txtfile:
    csvwriter = csv.writer(txtfile,delimiter=',')
    csvwriter.writerows([
            ['Election Result'],
            ['...............................'],
            [f'Total Votes: {total_votes}'],
            ['...............................']
    ])
    csvwriter.writerows(final_result)
    csvwriter.writerows([
            ['...............................'],
            [f'Winner: {winning_candidate}'],
            ['...............................']
    ])
