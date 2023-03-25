# Program:
# Programmer: Olivia Knestaut
# Date 2/15/2023


# Functions

def sumDigits(number):
    listOfDigits = []
    while len(str(number)) > 1:
        for num in str(number):
            listOfDigits.append(int(num))
        number = sum(listOfDigits)
        listOfDigits.clear()
    return number

def nameNumber(name):
    letterNums = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "D" : 4,
        "E" : 5,
        "F" : 8,
        "G" : 3,
        "H" : 5,
        "I" : 1,
        "J" : 1,
        "K" : 2,
        "L" : 3,
        "M" : 4,
        "N" : 5,
        "O" : 7,
        "P" : 8,
        "Q" : 1,
        "R" : 2,
        "S" : 3,
        "T" : 4,
        "U" : 6,
        "V" : 6,
        "W" : 6,
        "X" : 5,
        "Y" : 1,
        "Z" : 7
        }
    number = 0
    name = name.upper()
    for letter in name:
        try:
            #number += letterNums.get(letter)
            number += letterNums[letter]
        except:
            number += 0
    number = sumDigits(number)
    return number

def prediction(number):
    predictions = {
        1 : "A person who is successful in personal ambitions.",
        2 : "A gentle and artistic person.",
        3 : "A success in their professional career.",
        4 : "An unlucky person who much put in extra work for success.",
        5 : "A lucky person who leads an unconventional life.",
        6 : "A person who commands the respect of others.",
        7 : "A person who has a strong inner spirit.",
        8 : "A person who is misunderstood by others and is not respected for their success.",
        9 : "A person who is more successful in matters of the material than spiritual."
        }
    return predictions.get(number)

# Main Script
if __name__ == "__main__":
    # code for the main script goes under this line, all indented
    print ("Welcome to Name Number Generator")
    name = input("Enter Your Name: ")
    
    print ("Your Name Number is", nameNumber(name))
    print ("We predict you are:")
    print (prediction(nameNumber(name)))
    