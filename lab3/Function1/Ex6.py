def reve():
    s = input("Sentences: ")
    str = s.split()
    rev = ' '.join(reversed(str))
    print("Reversed sentences: " + rev)

reve()
