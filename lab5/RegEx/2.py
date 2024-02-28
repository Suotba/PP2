import re

file = open('row.txt', 'r')

w = file.read()

l = list(w.split('\n'))

for i in range(len(l)-1):
    p = re.search(".*abb.*|.*abbb.*",l[i])
    if p: 
        print("Need output 'ab*' in "  + str(i+1) + "th row: " + p.group())


