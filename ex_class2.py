import re

stroka = 'App/Data/Local/Programs/Python/Python39'
result = re.split(r'/', stroka)
print(result)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def decorator(func):
    def wrapper():
        print('Create...')
        a1 = []
        for i in list1:
            if i % 2 !=0:
                a1.append(i)
        return a1
    return wrapper

@decorator
def my_func1():
    return list1

print(my_func1())


class Car:
    brand: str
    model: str
    issue_year: str
    sk: float

    def __init__(self, brand, model, issue_year, sk=0):
        self.__brand = brand
        self.__model = model
        self.__issue_year = issue_year
        self.__sk = sk

    def upsk(self):
        self.__sk += 5
        return self.__sk

    def downsk(self):
        self.__sk -= 5
        return self.__sk

    def stopsk(self):
        return 0

    def sk1(self):
        return self.__sk

    def sk2(self):
        self.__sk *= -1
        return self.__sk


a1 = Car('citroen', 'C5', 2012, 98.6)
print(a1.upsk())
print(a1.downsk())
print(a1.stopsk())
print(a1.sk1())
print(a1.sk2())
a2 = Car('citroen', 'C5', 2012)
print(a2.upsk())
