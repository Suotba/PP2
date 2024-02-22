s = str(input())

s_lower = ""
for i in s:
    s_lower += i.lower()

s_reversed = ''.join(reversed(s_lower))

if s_lower == s_reversed:
    print("True")
else:
    print("False")

