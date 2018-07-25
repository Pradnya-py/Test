# Here I have counted highest frequency word in a file

fo = open("poem.txt", "r")

line = fo.readlines()

word_list = [word for i in line for word in i.split()]

print "wordlist > \n ", word_list

print "Total words are >", len(word_list)

map = {}

for outer in range(len(word_list)):
    count = 0
    for inner in range(len(word_list)):
         if word_list[outer]== word_list[inner]:
            count +=1



    key = str(word_list[outer])

    map[key]= count;

value1= max(map.values())

for key, value in map.items():
    if value == value1:
        print "The high frequency word is: '%s' \n with frequency> %d" %(key,value1)




