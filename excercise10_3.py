from string import punctuation, whitespace, digits
ignore = punctuation + whitespace + digits

file = raw_input("Enter file name")

fh = open(file)
fre_ch ={}
sort_fre_ch=[]
lines = fh.read()
lines =lines.translate(None,ignore)
lower_lines=lines.lower()

for c in lower_lines:
    fre_ch[c] = fre_ch.get(c,0)+1

for i,j in fre_ch.items():
    sort_fre_ch.append((j,i))

sort_fre_ch.sort(reverse= True)

for i,j in sort_fre_ch:
    print j,i