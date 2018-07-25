import re
exp = raw_input("Enter regular expression: ")
fh = open("mbox","r")
count = 0

for line in fh:
    stuff = re.findall(exp,line)
    if len(stuff)>0:
        count = count+1


print "mbox.txt had %d lines that matched %s " %(count,exp)

