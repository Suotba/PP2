l = ['jdm','GTR',38,35]

with open('test.txt','a') as file:
    for i in l:
        file.write(str(i) + ',' + ' ')