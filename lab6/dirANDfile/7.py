with open('test.txt','r') as file:
    content = file.read()
    
with open('exampl.txt','a') as file:
    for i in content:
        file.write(str(i))

"""
We can you this, but this method work when file not exist. It creat new file and add content
with open('exampl.txt','w') as file:
    for i in content:
        file.write(str(i))
"""