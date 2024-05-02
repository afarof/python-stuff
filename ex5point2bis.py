# simple exercise in while loops. pulls out & displays largest and smallest number of a set of integers inputted by user

# being picky about text displaying properly in terminal
import textwrap

print()
print(textwrap.fill("This script identifies the largest and smallest numbers among those integers you choose to input. Type 'done' to obtain the result."))

largest = None
smallest = None
numbers = []


while True: 
    
    rawnum = input("Enter a number: ")
    if rawnum == "done":
        break
        
# error checking user input
    try:
        num = int(rawnum) 
    except:
        print("Invalid input")
        num = None
        continue
        
    else: 
        if num is None:
            continue
        elif largest is None or num > largest:
            largest = num
        elif smallest is None or num < smallest:
            smallest = num  
    
    numbers.append(num)

print("Among the numbers", numbers, "the largest number is ", largest)
print("The smallest number is ", smallest)