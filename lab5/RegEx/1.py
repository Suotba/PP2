import re

file = open('row.txt', 'r')

s = file.read()

l = list(s.split('\n'))

for i in range(len(l)-1):
    k = re.search(".*a.*", l[i])
    if k :
        print("Found in " + str(i+1) + "th row: " + k.group())
