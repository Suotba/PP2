class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2


length_of_square = float(input("Length of the square: "))
square_obj = Square(length_of_square)

print("Area of shape:", Shape().area())
print("Area of square ", square_obj.area())
