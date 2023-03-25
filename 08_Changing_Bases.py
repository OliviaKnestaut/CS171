# Program: Converts Number to equivalent value with specified base
# Programmer: Olivia Knestaut
# Date: 3/14/2023

# FUNCTION DEFINITION
"""
    Purpose:
    Converts a given value into its equivalent value with a given (different) base

    Parameters:
    number -- integer between 1 and 1000 inclusive to find the equivalent of
    base -- integer between 2 and 9 inclusive to be the new base

    Return Value:
    equivalent number of different base as a string
    """
    
def convertToBase(number, base):
    if number / base == 0:
        MSD = number % base
        return ""
    else:
        result = int(number / base)
        LSD = int(number % base)
        return "%s%d" %(convertToBase(result, base), LSD)

    
# MAIN

if __name__ == "__main__" :
    
    # Keeps code looping if user inputs "y" later
    runCodeTrue = True
    while runCodeTrue:
        
        # Takes input number
        number = 0
        while number > 1000 or number < 1:
            try:
                number = int(input("Enter an integer between 1 and 1000: "))
                if number > 1000 or number < 1:
                    print ("Error: you entered a value out of range. Try again.")
            except:
                print("Invalid input: an integer value was expected. Try again.")
            
        # Takes input base
        base = 0
        while base > 9 or base < 2:
            try:
                base = int(input("Enter an integer between 2 and 9: "))
                if base > 9 or base < 2:
                    print ("Error: you entered a value out of range. Try again.")
            except:
                print("Invalid input: an integer value was expected. Try again.")
        
        #Runs function
        print("The equivalent of %d in base %d is %s" %(number, base, convertToBase(number, base)))
        
        #Reruns or stops program
        yOrn = input("Do you have another number to convert (Y / N)? ")
        while yOrn.upper() != "Y" and yOrn.upper() != "N":
            print("Error: Please enter Y or N. Try again.")
            yOrn = input("Do you have another number to convert (Y / N)? ")

        if yOrn.upper() == "Y":
            runCodeTrue = True
        elif yOrn.upper() == "N":
            runCodeTrue = False
            print("OK, Good-bye!")
            