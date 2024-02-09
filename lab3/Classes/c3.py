class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.length = a
        self.width = b

    def area(self):
        return self.length * self.width


a = float(input("Length of the rectangle: "))
b = float(input("Width of the rectangle: "))

rect = Rectangle(a,b)

print("Area of rectangle", rect.area())
