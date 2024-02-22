n = input()
n_list = list(map(int, n.split()))

multi_of_list = 1
for i in n_list:
    multi_of_list *=i

print (multi_of_list)