class Rectangle:
    def __init__(self):
        self.length = 10
        if self.width == "":
            self.width = self.length
        else:
            self.width = self.length * 2
    def area(self):
        space = self.length * self.width
        return space
    def perimeter(self):
        peri = 2 * (self.length + self.width)
        return peri

class Square(Rectangle):
    def __init__(self):
        self.length = 10

class Cube(Square):
    def __init__(self):
        self.length = 10
    def surfaceArea(self):
        space = Square.area(self)
        surfarea = space * 6
        return surfarea

cube = Cube()
cube.length = 3
cube.width = 3

print("The cubes area " + str(cube.area()))
print("The cubes perimeter " + str(cube.perimeter()))
print("The cubes surface area " + str(cube.surfaceArea()))