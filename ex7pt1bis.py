#simple exercise in pulling data from a file in the same directory and converting all lowercase letters to uppercase, then printing the resulting all-caps text

fname = input("Enter file name: ")
fhandle = open(fname)

lowertext = fhandle.read()
striptext = lowertext.strip()
uppertext = striptext.upper()
print(uppertext)