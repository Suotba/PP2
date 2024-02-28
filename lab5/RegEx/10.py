import re
file = open('row.txt', 'r')

w = file.read()

str = ""
for i in range(0, len(w)-1):
    if w[i] != " " and ((w[i + 1] >= 'A' and w[i + 1] <= 'Z') or (w[i + 1] >= 'А' and w[i + 1] <= 'Я')):
        str += (w[i].lower() + '_')
    elif w[i] == ' ':
        str += '_'
    else:
        str+= w[i].lower()
print(str)

