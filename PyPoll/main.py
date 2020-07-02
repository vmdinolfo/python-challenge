#import modules to create directories and read csv files
import os
import pandas as pd

#assign file to variable and read csv file
file = "Resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"
poll_df = pd.read_csv(file)

#open / create txt file 
output_file = os.path.join("analysis","poll_results.txt")
opened_file = open(output_file, 'w')

#Begin Election Results Summary
#find sum of all votes
total_votes = poll_df["Voter ID"].count()

#Find Candidates, vote %, and votes per candidate
#print(poll_df["Candidate"].unique())

khan_df = poll_df.loc[poll_df["Candidate"] == "Khan"]
khan_vote = khan_df["Candidate"].count()
khan_pct = round((khan_vote / total_votes) * 100, 2)
#print(khan_vote)
#print(khan_pct)

correy_df = poll_df.loc[poll_df["Candidate"] == "Correy"]
correy_vote = correy_df["Candidate"].count()
correy_pct = round((correy_vote / total_votes) * 100, 2)
#print(correy_vote)
#print(correy_pct)

li_df = poll_df.loc[poll_df["Candidate"] == "Li"]
li_vote = li_df["Candidate"].count()
li_pct = round((li_vote / total_votes) * 100, 2)
#print(li_vote)
#print(li_pct)

otooley_df = poll_df.loc[poll_df["Candidate"] == "O'Tooley"]
otooley_vote = otooley_df["Candidate"].count()
otooley_pct = round((otooley_vote / total_votes) * 100, 2)
#print(otooley_vote)
#print(otooley_pct)

#create vote total df
vote_summary = { "Candidate" : ["Khan", "Correy", "Li", "O'Tooley"],
                    "Votes" : [khan_vote, correy_vote, li_vote, otooley_vote]
                    }
vote_summary_df = pd.DataFrame.from_dict(vote_summary, orient='index').transpose()      #code to take dictionary of list to dataframe https://stackoverflow.com/questions/42869544/dictionary-of-lists-to-dataframe

#find winner
win_vote = vote_summary_df["Votes"].max()
winner = vote_summary_df.loc[vote_summary_df["Votes"] == win_vote, :]

#print results to terminal
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
print(f"Khan: {khan_pct}% ({khan_vote})")
print(f"Correy: {correy_pct}% ({correy_vote})")
print(f"Li: {li_pct}% ({li_vote})")
print(f"O'Tooley: {otooley_pct}% ({otooley_vote})")
print("----------------------------------------")
print(f"Winner: {winner.iloc[0]['Candidate']}")
print("----------------------------------------")

#write to file
opened_file.write("----------------------------------------\n")
opened_file.write("Election Results\n")
opened_file.write("----------------------------------------\n")
opened_file.write(f"Total Votes: {total_votes}\n")
opened_file.write(f"Khan: {khan_pct}% ({khan_vote})\n")
opened_file.write(f"Correy: {correy_pct}% ({correy_vote})\n")
opened_file.write(f"Li: {li_pct}% ({li_vote})\n")
opened_file.write(f"O'Tooley: {otooley_pct}% ({otooley_vote})\n")
opened_file.write("----------------------------------------\n")
opened_file.write(f"Winner: {winner.iloc[0]['Candidate']}\n")
opened_file.write("----------------------------------------\n")

#close file
opened_file.close()


