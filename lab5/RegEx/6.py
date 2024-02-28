import re

file = open('row.txt', 'r')

w = file.read()

l = list(w.split('\n'))

str = ""

for i in range(len(l)-1):
    if w[i] == ' ' or w[i] == ',' or w[i] == '.':
        str += ":"
    else : 
        str+=w[i]
print(str)
