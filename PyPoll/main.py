import os
import csv

#Set file paths
input_path = os.path.join("..","..","WUSTL201904DATA2","02-Homework","03-Python","Instructions","PyPoll","Resources","election_data.csv")
output_path = "pypoll.txt"

#Set Variables
Votes = []
Candidate_List = []
Vote_Count = 0
Candidate_Index = 0
Candidate_Votes = []
Vote_Percent = 0
Candidate_Percent = []
Highest_Vote = 0

with open(input_path) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    #Put all votes into list with candidate names
    for row in reader:
        Votes.append(row[2])

    #Total Votes
    Total_Votes = len(Votes)

    #Put each candidate name into list
    for i in Votes:
        if i not in Candidate_List:
            Candidate_List.append(i)

    #Set statistics for each candidate
    for candidate in Candidate_List:
        
        #Find number of votes for current candidate and add to list
        for i in Votes:
            if i == Candidate_List[Candidate_Index]:
                Vote_Count = Vote_Count + 1
        Candidate_Votes.append(Vote_Count)
       
        #Calculate vote percentage of each candidate and insert into list
        Vote_Percent = Vote_Count/Total_Votes*100
        Candidate_Percent.append(Vote_Percent)
        
        #Set variables for next candidate
        Vote_Percent = 0
        Vote_Count = 0

        #Find the winner
        if Candidate_Votes[Candidate_Index] > Highest_Vote:
            Highest_Vote = Candidate_Votes[Candidate_Index]
            Winner = Candidate_List[Candidate_Index]
        
        Candidate_Index = Candidate_Index + 1

    output = (
        "Election Results\n"
        "------------------------------\n"
        f"Total Votes: {Total_Votes}\n"
        "------------------------------\n"
        f"{Candidate_List[0]}: {Candidate_Percent[0]:.3f}% ({Candidate_Votes[0]})\n"
        f"{Candidate_List[1]}: {Candidate_Percent[1]:.3f}% ({Candidate_Votes[1]})\n"
        f"{Candidate_List[2]}: {Candidate_Percent[2]:.3f}% ({Candidate_Votes[2]})\n"
        f"{Candidate_List[3]}: {Candidate_Percent[3]:.3f}% ({Candidate_Votes[3]})\n"
        "------------------------------\n"
        f"Winner: {Winner}\n"
        "------------------------------")

    print(output)

with open(output_path, 'w', newline='') as txt_output:
    txt_output.write(output)
    


    
