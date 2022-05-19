import datetime
import re


class Cheese:
    name2: str
    weight: float
    issue_date: datetime.date
    expiry_date: datetime.date

    def __init__(self, name2, weight, issue_date, expiry_date):
        self.__name2 = name2
        self.__weight = weight
        self.__issue_date = issue_date
        self.expiry_date = expiry_date

    def get_name2(self):
        return self.__name2

    def set_name2(self, a):
        self.__name2 = a

    def get_weight(self):
        return self.__weight

    def set_weight(self, b):
        self.__weight = b

    def get_issue_date(self):
        return self.__issue_date

    def set_issue_date(self, c):
        self.__issue_date = c

    def info1(self):
        y1 = datetime.datetime.now()
        y3 = self.expiry_date
        if y1.date() < y3:
            print(f'Сыр годен')
        else:
            print(f'Сыр не годен')

    def info2(self):
        str1 = f'Сыр {self.__name2} весом {self.__weight} кг'
        result = re.findall(r'[0]', str1)
        if result == []:
            print(str1)
        else:
            print('Ты не взял сыр')



ch = Cheese('Camamber', 5, datetime.date(2022, 3, 21), datetime.date(2022, 5, 26))
print(ch.get_issue_date())
ch.info1()
ch.info2()
ch.set_weight(0)
ch.info2()
