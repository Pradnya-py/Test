import re
file = raw_input("Enter file name")
fh = open(file,"r")

count = 0
total =0

for line in fh:
    stuff = re.findall('New Revision: ([0-9]+)',line)
    if len(stuff)>0:
        total = total + float(stuff[0])
        count = count+1

print total/count