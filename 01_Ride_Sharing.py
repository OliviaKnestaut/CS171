#CS 171 - Homework 1 - Part 2
#Purpose:  This program calculates rider cost and diver payout for a ride share service
#Author:   Olivia Knestaut
#Date:     1/15/2023


# Define required functions here
def calculateFare(miles):
    return float(1.25 * miles)
  
def calculatePayout(dollars):
    return float((dollars * .8) - 1)

# Get input from the user
miles = int(input("Enter trip distance in miles: "))

# Call the functions that perfom the calculations
dollars = calculateFare(miles)
payout = calculatePayout(dollars)

# Display the results
print ("Rider should pay $", dollars,  "for this trip.")
print ("Driver will earn $", payout, "for this trip.")