import math

n = int(input("Number of sides: "))
l = int(input("Length of a side: "))

t = n * (l**2)

e = 4 * math.tan(math.pi / n)

s = t / e

print("Area of the polygon is:", s)
