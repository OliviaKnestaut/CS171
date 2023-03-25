# Program: Finds most and least popular toys from input toy list
# Programmer: Olivia Knestaut
# Date: 1/30/2023

print("Most popular toy of the year")

numToys = int(input("How many toys are in this year's list:"))
popularToys = [ input("Enter the name of toy #%d:" %(x+1)) for x in range (0, numToys) ]
totalVotes = [ int(input("Enter total votes for %s:" %(popularToys[x]))) for x in range (0, numToys) ]

# Total Votes
print("Total votes received: %d votes." %(sum(totalVotes)))

# Most Popular
print("%s has been selected as the most popular toy with a total of %d votes." %( popularToys[totalVotes.index(max(totalVotes))], max(totalVotes)))
print("That is %.2f%% of the votes." %((max(totalVotes)/sum(totalVotes))*100))

# Least Popular
print("%s received the least number of votes with a total of %d votes." %( popularToys[totalVotes.index(min(totalVotes))], min(totalVotes)))
print("That is %.2f%% of the votes." %((min(totalVotes)/sum(totalVotes))*100))
