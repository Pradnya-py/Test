# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with 'From', then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).
fn = raw_input("Enter file name")

fh = open(fn,"r")
days ={}
words = []
for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    name = words[2]
    days[name]=days.get(name,0) +1

print days
