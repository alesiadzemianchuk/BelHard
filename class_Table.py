class Table:
    color: str
    height1: float
    forma: str
    issue_year: int

    def __init__(self, color, height1, forma, issue_year):
        self.__color = color
        self.__height1 = height1
        self.__forma = forma
        self.issue_year = issue_year

    def get_color(self):
        return self.__color


    def set_color(self, a):
        self.__color = a

    def get_height1(self):
        return self.__height1

    def set_height1(self, b):
        self.__height1 = b

    def get_forma(self):
        return self.__forma

    def set_forma(self, c):
        self.__forma = c

    def info1(self):
        return f'Table is {self.__color} and form is {self.__forma}, issue_year is {self.issue_year}'

    def info2(self):
        if self.issue_year < 2000:
            return f"Table is very old"
        if self.__height1 < 1:
            return f"Table is for baby"
        else:
            return f"Table is normal"


a = Table('black', 1.20, 'rund', 2015)
print(a.get_color())
a.color = 'pink'
print(a.color)
print(a.get_color())
a.set_color('red')
print(a.get_color())
print(a.issue_year)
print(a.get_height1())
a.set_height1(1.3)
print(a.get_height1())
print(a.info1())
print(a.info2())

