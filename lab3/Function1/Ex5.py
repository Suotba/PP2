from itertools import permutations
def permu(str):  
    perList = permutations(str)
    
    for perm in list(perList):
        print(''.join(perm))
       
str = input()
permu(str)



