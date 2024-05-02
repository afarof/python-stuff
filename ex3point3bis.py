#exercise in converting a student's score to a floating point number and then printing the equivalent letter grade

score = input("Enter your score on a scale of 0 to 1: ")

# error-checking the input

try:
    flinput = float(score)
    
except:
    print("Score is not a number")
    quit() 
    
if flinput < 0.0 or flinput > 1.0:
    print("Score is out of range")
    quit()
    
#converting score to a letter grade and printing result
else:    
    if flinput >= 0.9:
        grade = "A"
    elif flinput >= 0.8:
        grade = "B"
    elif flinput >= 0.7:
        grade = "C"
    elif flinput >= 0.6:
        grade = "D"
    elif flinput < 0.6: 
        grade = "F"

print("Letter grade is", grade)