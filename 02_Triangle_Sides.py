# purpose:
# programmer: Olivia Knestaut
# date: 1/23/2023

import math

# defined function
def findSideC(sideA, sideB, angleInDegrees):
    angleInRadians = math.radians(angleInDegrees)
    return math.sqrt( math.pow(sideA, 2) + math.pow(sideB, 2) - (2 * sideA * sideB * math.cos(angleInRadians)))

# main script
if __name__ == "__main__" :
    
    sideA = int (input ("Enter length of side A: "))
    sideB = int (input ("Enter length of side B: "))
    angleInDegrees = int (input ("Enter angle between A and B (in degrees): "))
    
    sideC = findSideC(sideA, sideB, angleInDegrees)
    
    print("The length of side C of this triangle is", sideC)

