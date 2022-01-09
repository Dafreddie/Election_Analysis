# 1. The data we need to retrieve
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Resources", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Make a list of canadites
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning canadite and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    
    #Print each row in the csv file
    for row in file_reader:
        # Add to the toal vote counter
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        vote = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(vote) / float(total_votes) * 100
    
        # Votes to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({vote:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if (vote > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning count = votes and winning percentage 
            # Vote percentage
            winning_count = vote
            winning_percentage = vote_percentage
            # Set the winning canadidate equal to the condidates name
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)