from abc import abstractmethod
import math


class Animal:
    name: str

    def __init__(self, some_name):
        self.name = some_name

    @abstractmethod
    def says(self):
        pass

class Cat(Animal):

    def says(self):
        return f"{self.name} - кошка. Говорит МЯУ!"

class Dog(Animal):

    def says(self):
        return f"{self.name} - собака. Говорит ГАВ!"

class Cow(Animal):

    def says(self):
        return f"{self.name} - корова. Делает МУ!"

c1 = Cat('Мурка')
print(c1.says())
d1 = Dog('Тузик')
print(d1.says())
p1 = Cow('Зорька')
print(p1.says())


class Shape:

    @abstractmethod
    def get_perimetr(self):
        pass

    @abstractmethod
    def get_square(self):
        pass

class Circle(Shape):
    r: float

    def __init__(self, r):
        self.r = r

    def get_perimetr(self):
        return 2 * math.pi * self.r

    def get_square(self):
        return math.pi * self.r ** 2

class Rectangle(Shape):
    a: float
    b: float

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_square(self):
        return self.a * self.b

    def get_perimetr(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)



c1 = Circle(1)
print("Периметр окружности P=", c1.get_perimetr())
print("Площадь круга S=", c1.get_square())
c2 = Rectangle(2, 4)
print("Периметр прямоугольника P=", c2.get_perimetr())
print("Площадь прямоугольника S=", c2.get_square())
c3 = Square(5)
print("Периметр квадрата P=", c3.get_perimetr())
print("Площадь квадрата S=", c3.get_square())

