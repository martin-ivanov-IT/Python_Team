from math import pi
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        area = pi*self.r*self.r
        print(f"area: {area}")
        return area

c = Circle(3)
c.area()