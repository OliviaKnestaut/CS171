# Purpose: Calculate cost of carpet replacement
# Author: Olivia Knestaut
# Date: 1/23/2023

#defined function
def calculateCost(carpetPrice, roomWidth, roomLength):
    squareFeet = float(roomWidth * roomLength)
    carpetNeeded = squareFeet * 1.15
    carpetCost = carpetNeeded * carpetPrice
    laborCost = squareFeet * 0.85
    salesTax = (carpetCost + laborCost) * .08
    return carpetCost + laborCost + salesTax

# main script 
if __name__ == "__main__":
    
    carpetPrice = float( input("Enter the carpet price per square foot: "))
    roomWidth = int( input("Enter the room width in feet: "))
    roomLength = int( input("Enter the room length in feet: "))
    
    totalCost = calculateCost(carpetPrice, roomWidth, roomLength)
    
    print ("The total cost of replacing the carpet for this room is", '{:.2f}'.format(totalCost), "dollars.")
    
    