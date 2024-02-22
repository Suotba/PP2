def gen_3(n):
    res_3 = []
    for i in range(1, n):
        if i % 3 == 0:
              yield i

def gen_4(n):
    res_4 = []
    for i in range(1, n):
        if i % 4 == 0:
            yield i
    

n = int(input("Number: "))

result = list(gen_3(n))
res = list(gen_4(n))

print("Divisible by 3:", list(result))
print("Divisible by 4:", list(res))
