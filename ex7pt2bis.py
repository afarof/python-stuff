#finding the average spam confidence in a file full of header information stripped from a set of emails. file is mbox-short.txt

fname = input("Enter filename of the mailbox dataset: ")
fhand = open(fname)
count = 0
totes = 0

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    colon = line.find(":")
    num = line[colon+1:].strip()
    flt = float(num)
    totes = totes + flt
    count = count + 1
    
average = totes / count
print("Average spam confidence:", average)
