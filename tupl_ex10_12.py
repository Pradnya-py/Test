
file = raw_input("Enter file name")

fh = open(file,"r")
name_count ={}
tup_name=[]
hour_count={}

for line in fh:
    if not line.startswith("From "):
        continue
    words=line.split()
    time = words[5]
    time = time.split(":")
    hour =time[0]
    hour_count[hour] = hour_count.get(hour,0)+1
    name = words[1]
    name_count[name]= name_count.get(name,0) +1

for n, j in name_count.items():
    tup_name.append((j,n))

tup_name.sort(reverse=True)

for n,j in tup_name[:1]:
    print j,n

for a,b in sorted(hour_count.items()):
    print a,b

