import re 

file  = open('row.txt', 'r')
w = file.read()

str = w[0].lower()
for i in range(1, len(w)):
    if w[i] == " " or w[i] == "_":
        continue
    elif w[i-1] == "\n":
        str+=w[i].lower()
        continue
    elif w[i-1] == " ":
        str+=w[i].upper()
        continue
    elif w[i] != " ":
        str+=w[i].lower()
print(str)
