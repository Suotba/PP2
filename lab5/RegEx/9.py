import re

with open('row.txt', 'r') as file:
    w = file.read()
    lines = w.split('\n')
    
for string in lines:
    str = ""
    for i in range(len(string) - 1):
        if string[i] != ' ' and ((string[i + 1] >= 'A' and string[i + 1] <= 'Z') or (string[i + 1] >= 'А' and string[i + 1] <= 'Я')):
            str += (string[i] + ' ')
        else:
            str += string[i]
    str += string[len(string) - 1]
    print(str)