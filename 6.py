lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
def func_1(lst):
    sum1 = 0
    for i in lst:
        if (i < 30) & (i % 3 ==0):
            print(i)
        else:
            sum1 = sum1 + i
    print(f'Сумма = {sum1}')

func_1(lst)


def sum_range(start, end):
    sum2 = 0
    if start > end:
        start, end = end, start
    for i in range(start, end+1):
        sum2 = sum2 + i
    print(sum2)

sum_range(8, 3)


def more_than_five(lst):
    lst2 = []
    for i in lst:
        if abs(i) > 5:
            lst2.append(i)
    print(lst2)

more_than_five(lst)


lst4 = [11, 5, 8, 32, 15, 3, 20, 139, 21, 4, 555, 9, 20]
def func_nech139(lst4):
    for i in lst4:
        if (i == 139):
            break
        elif (i % 2 == 1):
            print(i)

func_nech139(lst4)


lst5 = []
def range_1(a, b, c):
    for i in range(a, b+1, c):
        lst5.append(i)
    print(lst5)

range_1(2, 18, 4)


def month_to_season(n1):
    if n1 in (1, 2, 12):
        print('Зима')
    elif n1 in (3, 4, 5):
        print('Весна')
    elif n1 in (6, 7, 8):
        print('Лето')
    else:
        print('Осень')

n1 = int(input('Введите номер месяца '))
month_to_season(n1)
