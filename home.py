#вывести все числа меньше 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)


for i in range(len(a)):
    if a[i] < 5:
        print(a[i])

#вывести все четные числа пока не встретим 237
a1 = [1, 1, 2, 3, 5, 8, 13, 237, 21, 34, 55, 89]
for i in a1:
    if i == 237:
        break
    elif i % 2 == 0:
        print(i)


#убрать все большие буквы
a2 = 'ротошЛОшгозОШОугаозтсОДОцхцщоЬзшпр'
a3 = ''
for i in a2:
    if not i.isupper():
        a3 += i
print(a3)


#проверить, есть ли такой ник
a4 = ['alesia', 'nik', 'master']
b = input('Введите ник ')
while b not in a4:
    print('Неверный ник, вводи снова')
    b = input()
else:
    print(f'привет, {b}')


#найти наименьший делитель заданного числа
c1 = int(input('Введите целое число '))
c2 = []
for i in range(2, c1+1):
    if (c1 % i == 0):
        c2.append(i)
        print(c2)
        break


#посчитать количество цифр в числе
d1 = int(input('Введите число '))
count = 1
while(d1//10) > 0:
    count += 1
    d1 = d1 / 10
print(f'Количество цифр = {count}')


#найти числа, которые не делятся на 3 и на 2 записаны в столбец
for i in range(1, 51):
    if (i % 3 != 0) and (i % 2 != 0):
        print(i)

#найти числа, которые не делятся на 3 и на 2 записаны в строку
l1 = []
for i in range(1, 51):
    if (i % 3 != 0) and (i % 2 != 0):
        l1.append(i)
print(l1)


#посчитать стоимость посещения парка с любым количеством посетителей
age = input('Введите возраст посетителя либо оставьте пусто, если посетители закончились ')
summ = 0
while (age != ''):
    if (int(age) < 3):
        summ = summ
    elif 3 <= int(age) <= 12:
        summ = summ + 14
    elif int(age) >= 65:
        summ = summ +18
    else:
        summ = summ +23
    age = input('Введите возраст посетителя либо оставьте пусто, если посетители закончились ')

print(f'Сумма = {summ}')


#стоимость посещения парка с заданным количеством посетителей с разными возрастами
n = int(input('Введите количество посетителей '))
summ = 0
for i in range(n):
    age = int(input('Введите возраст посетителя  '))
    if (age < 3):
        summ = summ
    elif 3 <= age <= 12:
        summ = summ + 14
    elif age >= 65:
        summ = summ + 18
    else:
        summ = summ + 23
print(f'Сумма = {summ}')
