from Rectangle import Rectangle


class Parallelepiped(Rectangle):
    def __init__(self, lenght_input, width_input, height_input):
        super().__init__(lenght_input, width_input)
        self.height = height_input

    # def area(self):
    #     area = 2 * (self.lenght * self.width + self.lenght * self.height + self.width * self.height)
    #     print(f"area: {area}")
    #     return area

    def volume(self):
        volume = self.area() * self.height
        return volume


p = Parallelepiped(2, 3, 4)
print((p.volume()))
