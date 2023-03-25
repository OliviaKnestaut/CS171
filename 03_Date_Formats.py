# Program: takes date input in "mm/dd/yyyy" form and returns it in long form and international short form
# Programmer: Olivia Knestaut
# Date: 1/30/2023


# define the 2 required functions below this line
def dateLongForm (dateString):
    months = {'01' : 'January', '02' : 'February', '03' : 'March', '04' : 'April', '05' : 'May', '06' : 'June', '07' : 'July', '08' : 'August', '09' : 'September', '10' : 'October', '11' : 'November', '12' : 'December'}
    return "%s %s, %s" %(months[dateString[0:2]], dateString[4:5] if dateString[3:4] == "0" else dateString[3:5], dateString[6:])
    
def internationalShortForm (dateString):
    return "%s-%s-%s" %(dateString[3:5], dateString[0:2], dateString[8:])
    

# the main script 
if __name__ == "__main__":
    dateString = input("Enter a date in the following format (mm/dd/yyyy):")
    print ("Date long form:", dateLongForm(dateString))
    print ("International short form:", internationalShortForm (dateString))
    