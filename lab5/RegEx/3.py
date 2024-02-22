import re

word = input("Your string: ")
matches = []

p = re.compile(r'a' + '_'+'a', word )
matches.extend(p.findall(word))

print("Need output 'ab*':", matches)