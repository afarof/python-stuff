# exercise in defining functions, calculations, error-checking
# program calculates weekly pay based on user-inputted hours and rate, taking into account overtime pay past 40 hours

print("Enter your hours worked this week and your hourly rate in order to calculate your total pay.")

def computepay(h, r):
    if h <= 40:
        p = h * r
    else: 
        overtime = h - 40
        p = (40 * r) + (overtime * (r * 1.5))
    return p
        
hrs = input("Enter Hours:") 

# error-checking user input
try:
    h = float(hrs)
except: 
    print("Hours must be a number")
    quit()

rate = input("Enter hourly rate:")

# error checking here too    
try:
    r = float(rate)
except:
    print("Rate must be a number")
    quit()

p = computepay(h, r)
print("Total weekly pay is", p)
    