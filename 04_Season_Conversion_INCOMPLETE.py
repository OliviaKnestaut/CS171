#Program: Converts Dates to the Tamil season
#Programmer: Olivia Knestaut
#Date 2/8/2023

# defined functions

def monthNum(abbr):
    abbrLower = abbr.lower()
    if abbrLower in months.keys():
        return months[abbrLower]
    else:
        return 0

def tamilSeason(month,day):
    if (month == 4 and 15 <= day) or (month == 5) or (month == 6 and day <= 14):
        return 'MuthuVenil'
    elif (month == 6 and 15 <= day) or (month == 7) or (month == 8 and day <= 14):
        return 'Kaar'
    elif (month == 8 and 15 <= day) or (month == 9) or (month == 10 and day <= 14):
        return 'Kulir'
    elif (month == 10 and 15 <= day) or (month == 11) or (month == 12 and day <= 14):
        return 'MunPani'
    elif (month == 12 and 15 <= day) or (month == 1) or (month == 2 and day <= 14):
        return 'PinPani'
    elif (month == 2 and 15 <= day) or (month == 3) or (month == 4 and day <= 14):
        return 'IlaVenil'
    else:
        return 'Could not be found'

def validDay(month,day):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 0 < day and day <= 31:
            return True
        else:
            return False
    elif month == 2:
        if 0 < day and day <= 29:
            return True
        else:
            return False
    else:
        if 0 < day and day <= 30:
            return True
        else:
            return False
    

# main script  
if __name__ == "__main__":
    print ("Welcome to Tamil season converter.")
    months = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5, 
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12
    }
    
    abbr = input("Enter Month (three letter abbrv.): ")
    month = (monthNum(abbr))
    
    if month != 0:
        day = int(input("Enter Day (number): "))
        if validDay(month, day) :
            print('Tamil Season is', tamilSeason(month, day))
        else:
            print('Day Invalid')
    else:
        print('Month Invalid')        
 
    