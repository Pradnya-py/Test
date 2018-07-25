
# Program checks for lines which starts with from to list all sender,
# here string is used instead list as list will require more memory space
filehand = raw_input("Enter file name") # Enter file name
try:
    fi = open(filehand, "r")                # read file
except:
    print ("Enter file name")
    quit()

count = 0
for i in fi:
    if not i.startswith("From:"):       # Line starts with from
        count +=1
        continue

    h = i.find(" ")
    print i[h+1:]
print "There were total %d lines from 'from'" % count