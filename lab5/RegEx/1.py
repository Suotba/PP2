import re

word = input("Your string: ")

matches = re.findall("a+b*", word, flags=re.IGNORECASE)

print("Need output'ab*':", matches)
