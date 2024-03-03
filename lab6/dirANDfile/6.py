import os

for i in range(ord('A'), ord('Z')+1):
    file_name = chr(i) + '.txt'
    file = open(os.path.join('Way', file_name), 'w')    
    file.close()