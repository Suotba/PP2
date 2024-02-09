
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = (dx**2 + dy**2)
        corrent_distance = distance **0.5
        return corrent_distance


x1 = float(input("X1: "))
y1 = float(input("Y1: "))
point1 = Point(x1, y1)

x2 = float(input("X2: "))
y2 = float(input("Y2: "))
point2 = Point(x2, y2)

point1.show()

new_x1 = float(input(("New x1: ")))
new_y1 = float(input("New y1: "))
point1.move(new_x1, new_y1)
point1.show()

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")

