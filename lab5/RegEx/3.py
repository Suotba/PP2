import re

file = open('row.txt', 'r')

w = file.read()

l = list(w.split('\n'))

for i in range(len(l)-1):
    k = re.search(".*_[a-z].*|.*[a-z]_.*", l[i])
    if k :
        print("Found in " + str(i+1)+"th row : " + k.group())