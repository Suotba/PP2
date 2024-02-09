class StringPower:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("String: ")

    def printString(self):
        print("String in uppercase:", self.str.upper())


s_changer = StringPower()


s_changer.getString()


s_changer.printString()
