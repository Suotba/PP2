import re

word = input("Your string: ")

matches = re.findall("a+b*", word)

print("Need output'ab*':", matches)
