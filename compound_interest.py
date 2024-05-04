#calculating the compound interest of a loan, based on user input of the principal, yearly interest rate, and compounding period in years. Result is truncated to two decimal places.

from math import ceil

print()
print("Calculate the compound interest of a loan based on the principal, interest rate, and number of compounding periods:")

def compound_interest(principal, rate, time):
    # calculating the compound interest
    cilong = principal * ((1 + rate/100) ** time) - principal 
    # truncating/rounding the result to two decimal places
    ci = ceil(cilong * 100) / 100
    
    print("Total compound interest over", time, "compounding periods is: ", ci)
    
# requesting user input    
princ = input("Enter the principal: ")
principal = float(princ)

percrate = input("Enter the annual interest rate: ")
rate = float(percrate)

years = input("Enter the number of compounding periods (for example years, months, or weeks):")
time = int(years)

# calling function
compound_interest(principal, rate, time)
