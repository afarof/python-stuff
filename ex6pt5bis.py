#exercise in pulling data from a file in the same directory containing header info for a number of emails, then isolating a certain line from each header in order to output the X-DSPAM-Confidence number of each entry

fname = input("Enter file name: ")
fhandle = open(fname)

# finds and prints only the confidence numbers

for line in fhandle: 
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    colon = line.find(":")
    confnum = line[colon+1:].strip()
    flt = float(confnum)
    print(flt)
