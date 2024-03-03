with open('test.txt','r') as file:
    line = file.readlines()
    count = len(line)
    print("How many line:",count)
