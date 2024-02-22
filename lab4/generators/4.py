import math 
def gen(a,b):
    for i in range(math.ceil(a**(1/2)) , int(b**(1/2)+1)):
        yield i**2

a = int(input("Lower bound: "))
b= int(input("Upper bound: "))

e = gen(a,b)

print(f"All squares from {a} to {b}:",list(e))
