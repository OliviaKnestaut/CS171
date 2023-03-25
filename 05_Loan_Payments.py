# Program: Calculates Loan Payments
# Programmer: Olivia Knestaut
# Date: 2/13/2023


# Functions

def totalInterestPaid(loanValue, annualRate, numberOfPayments):
    monthlyPayment = (((0.01 * annualRate)/12) * loanValue) / (1 - (( 1 + ((0.01 * annualRate)/12)) ** (-numberOfPayments)))
    if monthlyPayment * numberOfPayments >= loanValue:
        monthlyInterest = loanValue * (0.01 * annualRate/12)
        Principal = (monthlyPayment - monthlyInterest) * numberOfPayments
        return (monthlyPayment * numberOfPayments) - loanValue
    
    return 

# Main Script

if __name__ == "__main__":

# Test Balance Input

    print("Balance due")
    while True:
        try:
            loanValue = float(input("Enter a value between 1000.00 and 100000.00: "))
        except ValueError:
            print("Invalid input. A numeric value was expected.")
        else:
            if 1000 <= loanValue <= 100000:
                break
            else:
                print("Error: value is out of bounds.")
    
    print()
    
# Test Number of Payments Input

    print("Total Number of Payments")
    while True:
        try:
            numberOfPayments = int(input("Enter a value between 12 and 120: "))
        except ValueError:
            print("Invalid input. An integer value was expected.")
        else:
            if 12 <= numberOfPayments <= 120:
                break
            else:
                print("Error: value is out of bounds.")
                
    print()
    
# Test Interest Rate Input
    
    print("Interest Rate")
    while True:
        try:
            annualRate = float(input("Enter a value between 1.60 and 18.50: "))
        except ValueError:
            print("Invalid input. A numeric value was expected.")
        else:
            if 1.60 <= annualRate <= 18.50:
                break
            else:
                print("Error: value is out of bounds.")
    print()
    
# Final Outputs
            
    print("%-14s $%.2f" %("Loan Amount:", loanValue))
    print("%-14s %.2f%%" % ("Interest Rate:", annualRate))
    print("%-14s %d" %("Payments Made:", numberOfPayments))
    print("%-14s $%.2f" % ("Interest Paid:", totalInterestPaid(loanValue, annualRate, numberOfPayments)))
    print("%-14s $%.2f" %("Total Paid:", (totalInterestPaid(loanValue, annualRate, numberOfPayments) + loanValue)))
