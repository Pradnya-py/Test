# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with 'X-DSPAM-Confidence:'
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence."""

#Input a file
ffile = raw_input("Enter a file name:")
if ffile == "na na boo boo":
		print ffile.upper(), "TO YOU- You have been PUNK'd "
		quit()
#check existance of the file, here it's 'short'
try:
	
    fo = open(ffile, "r")
except:
    print("File cannot be be opened")
    quit()
count = 0
line_count =0

for line in fo:
    nline = line.strip() 			# remove whiltespaces
    line_count += 1
    if "X-DSPAM-Confidence:" not in nline:		# To check string in the line
        continue
    count +=1
    fline= nline.find(": ")
    number = nline[fline+1:]			#get the number
    number = float(number)
    total =0.0
    total = total+number				# calculate sum of all available numbers
print "Total number of lines are", line_count
print "The average spam confidence is ", total/count
print "The number of lines for SPAM confidence are",count