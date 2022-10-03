from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def get_area(self):
        return self.side * self.height / 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.get_area()

        return total


shapes = [Rectangle(2, 3), Triangle(2, 3), Rectangle(6, 2)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
