# Write a program to open the file romeo.txt and read it line by line. For
# each line, split the line into a list of words using the split function. For
# each word, check to see if the word is already in a list. If the word is
# not in the list, add it to the list. When the program completes, sort
# and print the resulting words in alphabetical order.

fname = raw_input("Enter file:")
try:
    fhandler = open(fname,"r")
except:
    print "Please enter valid file name"
    quit()

words=[]
uniq_words=[]

for line in fhandler:           # split words
    word = line.split()
    for i in word:
        words.append(i)

for word in words:              #unique words
    if word in uniq_words:
        continue
    uniq_words.append(word)

for word in sorted(uniq_words): #print sorted list
    print word