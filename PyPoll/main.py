#MODULE 3 PYPOLL
import os
import csv

#initalize variable for calculation for the votes
totalVotes=0
#create dictionary for calculation for votes per candidate
candVotes={}


election_data = os.path.join('Resources/election_data.csv')
results=os.path.join('Analysis/results.txt')
#open and read csvfile
with open(election_data) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader= csv.reader(csvfile,delimiter=",")
    #skip first row
    next(csvreader)
   
    #read each row of data after the header
    for row in csvreader:
        #calculate total months
        totalVotes +=1
        #find the candidate name is column 3
        candidate= row[2]
        #separate candidate data
        if candidate not in candVotes:
            #initialize votes per candidate
            candVotes[candidate]=1
        else:
            #calculate the votes per candidates
            candVotes[candidate]+=1
#find the winner
winner = max(candVotes, key=candVotes.get)
#print AND export the table
#create list to export
#PRINT RESULTS

    #find candidate with the most votes
    
#print to terminal

#print results to a text file
with open(results,'w') as txt_file:
    ele_results=(
    "Election Results\n"
    "--------------------------------\n"
    f"Total Votes: {totalVotes}\n"
    "--------------------------------\n")
    print(ele_results)
    txt_file.write(ele_results)
    for candidate, votes in candVotes.items():
        #calculate the percent of votes per candidate
        votePercent=(votes/totalVotes)*100
        candidate_results=(
        f"{candidate}: {votePercent:.3f}% ({votes})\n")
        
        print(candidate_results)
        txt_file.write(candidate_results)
    winner=(
    "--------------------------------\n"
    f"Winner: {winner}\n"
    "--------------------------------\n")
    print(winner)
    txt_file.write(winner)
    
