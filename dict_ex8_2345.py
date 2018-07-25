# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with 'From', then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).
# Exercise 3: Write a program to read through a mail log, build a his-
# togram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.
# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dic-
# tionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.
# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

fn = raw_input("Enter file name")

fh = open(fn,"r")


days ={}
names ={}
words = []
domain = {}
flag = None
highest_count_name = ""

for line in fh:
    if not line.startswith("From "):
        continue

    words = line.split()
    name = words[1]
    names[name] = names.get(name, 0) + 1  # count how many messages have come from each email address

    schools = name.split("@")
    school= schools[1]
    domain[school]=domain.get(school,0)+1 #count how many messages have come from each domain


    day = words[2]
    days[day] = days.get(day, 0) + 1 #count how many messages have come each day


    if flag <= names[name]:                     # who has the most messages in the file
        flag = names[name]
        highest_count_name = name

print highest_count_name, flag
print days
print names
print domain
