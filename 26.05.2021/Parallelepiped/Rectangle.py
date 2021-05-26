class Rectangle:
    def __init__(self, lenght_input, width_input):
        self.lenght = lenght_input
        self.width = width_input

    def perimeter(self):
        return 2 * self.width + 2 * self.lenght

    def area(self):
        return self.width * self.lenght

    def display(self):
        print(f"width: {self.width} lenght: {self.lenght} P: {self.perimeter()} area: {self.area()}")
        return "width: {} lenght: {} P: {} area: {}".format(self.width, self.lenght, self.perimeter(), self.area())