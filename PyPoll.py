# The data we need to retrieve.
 # 1. The total number of votes
 # 2. A complete list of candidates who received votes
 # 3. The percentage of votes each candidate won
 # 4. The total number of votes each candidate won
 # 5. The winner of the election based on popular vote.
#Assign a variable for the filed to load the path.

file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election result and read the file.

#election_data = open(file_to_load, 'r')

#To do: perform analysis.
#Close the file.

#election_data.close()

#Open the election result and read the file.
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)



