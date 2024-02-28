import re

file = open('row.txt', 'r')

w = file.read()

list = list(w.split('\n'))

pattern = re.compile(r'[A-ZА-Я][^ [A-ZА-Я]*]*|^[A-ZА-Я][^ ]*')

for i in list:
    x = pattern.findall(i)
    print(x)