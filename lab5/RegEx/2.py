import re

word = input("Your string: ")
matches = []

for i in range(2, 4):
    p = re.compile(r'a' + 'b' * i, flags=re.IGNORECASE)
    matches.extend(p.findall(word))

print("Need output 'ab*':", matches)
