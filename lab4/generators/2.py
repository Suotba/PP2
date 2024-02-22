
def gener(n):
 
 for i in range(1, n):
     if i % 2 == 0:
         yield i

n = int(input("Number: "))

res = list(gener(n))

print("Even numbers: ",res)