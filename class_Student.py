from datetime import datetime
class Student:
    name1: str
    course1: int
    group1: int
    year_of_birth: int

    def __init__(self, name1, course1, group1, year_of_birth):
        self.__name1 = name1
        self.__course1 = course1
        self.__group1 = group1
        self.year_of_birth = year_of_birth

    def get_name1(self):
        return self.__name1

    def set_name1(self, a1):
        self.__name1 = a1

    def get_course1(self):
        return self.__course1

    def set_cource1(self, a2):
        self.__course1 = a2

    def get_group1(self):
        return self.__group1

    def set_group1(self, a3):
        self.__group1 = a3
        return self.__group1

    def info1(self):
        print(f'Student {self.__name1} is studying in the {self.__group1} group')

    def old1(self):
        y1 = datetime.now()
        return f'student {self.__name1} is {y1.year-self.year_of_birth} years old'


    name1 = property(get_name1, set_name1)

a1 = Student('Mark', 3, 14, 1999)
print(a1.get_name1())
a1.name1 = 'Nikol'
print(a1.name1)
print(a1.get_name1())
a1.group1 = 5
print(a1.group1)
print(a1.get_group1())
a1.set_group1(6)
print(a1.set_group1(6))
print(a1.get_group1())
a1.info1()
print(a1.old1())
