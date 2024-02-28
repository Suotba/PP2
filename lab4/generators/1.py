import math 
def gen(n):
    for i in range(1, int(n**(1/2)+1)):
        yield i**2

n = int(input("Number: "))
generator = list(gen(n))

print(f"Squares until {n}: {generator}")
