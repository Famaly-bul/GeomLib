import abc
import math

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Неверный радиус")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        sides = sorted([a, b, c])
        if any(not isinstance(x, (int, float)) for x in sides) or min(sides) <= 0:
            raise ValueError("Неправильные размеры сторон")
        elif sides[0] + sides[1] <= sides[2]:
            raise ValueError("Это не треугольник")
        self.a, self.b, self.c = sides

    def is_right_angled(self):
        #Проверяет, является ли треугольник прямоугольным
        return abs((self.a ** 2 + self.b ** 2) - self.c ** 2) < 1e-6

    def area(self):
        s = sum(self.__dict__.values()) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

