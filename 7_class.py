class Convert:

    def __init__(self, some_val):
        self.val = some_val

    def conv1(self):
        return f"В {self.val} килограммах количество футов = {self.val*2.204}"

    def conv2(self):
        return f"В {self.val} километрах количество метров = {self.val*1000}"

    def conv3(self):
        return f"В {self.val} дециметрах кубических количество литров = {self.val}"

    def get(self):
        return self.val

c1 = Convert(12)
print(c1.conv1())
c2 = Convert(5)
print(c2.conv2())
c3 = Convert(3)
print(c3.conv3())


class Nicola:

    __slots__ = ["name1", "age1"]

    def __init__(self, some_name1, some_age1):
        self.name1 = some_name1
        self.age1 = some_age1

    def nik(self):
        if self.name1 != 'Николай':
            return f"Я не {self.name1}, а Николай, мне {self.age1} лет"
        else:
            return f"Я {self.name1}, мне {self.age1} лет"

n1 = Nicola('Николай', 12)
print(n1.nik())
n2 = Nicola('Максим', 35)
print(n2.nik())


class Soda:

    def __init__(self, some_ingr = None):
        self.ingr = some_ingr

    def show_my_drink(self):
        if self.ingr is not None:
            return f"Газировка и {self.ingr}"
        else:
            return f"Обычная газировка"


ingr1 = Soda()
print(ingr1.show_my_drink())
ingr2 = Soda('лимон')
print(ingr2.show_my_drink())



