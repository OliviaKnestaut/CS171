# Program: Calculates BAC based on inputs and prints chart of impairments
# Programmer: Olivia Knestaut
# Date: 3/1/2023

'''
    Purpose of Function: compute blood alcohol content
    @param: 
        drinks: integer, number of drinks
        weight: integer, weight in pounds
        duration: integer, time in minutes since last drink
    @return: blood alcohol content as a tuple with both male BAC and female BAC
'''

def computeBloodAlcoholConcentration(drinks, weight, duration):
    maleBac = ((drinks / weight) * 3.8) - (.01 * duration/40)
    if maleBac < 0:
        maleBac = 0
    femaleBac = ((drinks / weight) * 4.5) - (.01 * duration/40)
    if femaleBac < 0:
        femaleBac = 0
    bac = (maleBac, femaleBac)
    return bac
    
    
'''
    Purpose of Function: Return string describing impairment
    @param: 
        bac: float, blood alcohol content
    @return: blood alcohol content as a tuple with both male BAC and female BAC
'''

def impairment(bac):
    if bac == 0:
        return "Safe to Drive"
    elif 0 < bac < 0.04:
        return "Some Impairment"
    elif 0.04 <= bac < 0.08:
        return "Driving Skills Significantly Affected"
    elif 0.08 <= bac < 0.1:
        return "Criminal Penalties in Most US States"
    elif 0.1 <= bac < 0.3:
        return "Legally Intoxicated - Criminal Penalties in All US States"
    else:
        return "Death is Possible!"
  
    
'''
    Purpose of Function: Print chart with impairment information
    @param: 
        weight: integer, weight in pounds
        duration: integer, time in minutes since last drink
        sex: string, male or female
    @return: none
'''

def showImpairmentChart(weight, duration, sex):
    print("%d pounds, %s, %d minute(s) since last drink" %(weight, sex, duration))
    print("#drinks   BAC       Status")
    if sex == "male":
        for x in range (12):
            print ("%-9d %-9.4f %s" %(x, computeBloodAlcoholConcentration(x, weight, duration)[0], impairment(computeBloodAlcoholConcentration(x, weight, duration)[0])))
    else:
        for x in range (12):
            print ("%-9d %-9.4f %s" %(x, computeBloodAlcoholConcentration(x, weight, duration)[1], impairment(computeBloodAlcoholConcentration(x, weight, duration)[1])))


'''
    Purpose of Function: recieve integer from user within given bounds
    @param: 
        lower: lower bound for input
        upper: upper bound for input 
    @return: entered number, when it fits bounds
'''
    
def promptForInteger (lower, upper):
    num_entered = -1
    while num_entered < lower or num_entered > upper:
        try:
            num_entered = int(input())
            if lower <= num_entered <= upper:
                break
            else:
                print('Error: value out of bounds')
        except:
            print('Error: An integer value was expected. Try again')
    return num_entered
   
    
'''
    Purpose of Function: prompt user for sex of either "M" or "F"
    @param: none 
    @return: entered letter, either "M" or "F"
'''

def promptForMorF():
    sex = input()
    sex = sex.upper()
    while sex != "M" and sex != "F":
        try:
            print('Error: You must enter M or F')
            sex = input()
            sex = sex.upper()
        except:
            print('Error: You must enter M or F')
            sex = input()
            sex = sex.upper()
    if sex == "M":
        return "male"
    else:
        return "female"


#driver to call and organize all other functions
if __name__ == '__main__':
    print('Enter your weight (in lbs): ')
    weight = promptForInteger(0, 500)
    print('How many minutes has it been since your last drink? ')
    duration = promptForInteger(0, 300)
    print('Enter your sex as M or F: ')
    sex = promptForMorF()
    showImpairmentChart(weight, duration, sex)