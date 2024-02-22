s = str(input())

count_of_lower = 0

of_upper = 0

for i in s:
    if i.islower():
        count_of_lower +=1
    else:
        of_upper +=1

print("Lowercase count:", count_of_lower)
print("Uppercase count:", of_upper) 