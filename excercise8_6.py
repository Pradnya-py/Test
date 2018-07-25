# Find Maximum and Minimum number
numbers = []
while True:
    no = raw_input("Enter number")
    if no == "done":
        break
    try:
        no = int(no)        # Check for valid integer
    except:
        print "Invalid Input"
        continue
    numbers.append(no)

print "Maximum", max(numbers)
print "Minimum", min(numbers)

