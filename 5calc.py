def culc1(a, b, c):
    if c == '+':
        result = a + b
        print(result)
    elif c == '-':
        result = a - b
        print(result)
    elif c == '*':
        result = a * b
        print(result)
    else:
        result = 0
        try:
            result = a / b
        except ZeroDivisionError:
            print('нельзя делить на ноль')
        print(f'{result}')

    # try:
    #      if b == 0:
    #          raise ZeroDivisionError('er')
    # except ZeroDivisionError:
    #      print('null')



    d1 = {0: 'ноль',
          1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
          10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
          16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
          40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто', 100: 'сто',
          200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот',
          900: 'девятьсот', 1000: 'одна тысяча'}
    if type(result) == float:
        print("Это дробное число")

    if (result < 0):
        result *= -1
        print("минус")
    if (result > 100 and result % 100 > 19 and result % 10 >= 0):
        print(f'{d1[result - result % 100]} {d1[result % 100 - result % 10]} {d1[result % 10]}')
    elif (result > 100 and result % 100 < 20):
        print(f'{d1[result - result % 100]} {d1[result % 100]}')
    elif (result > 20 and result < 100 and result % 10 > 0):
        print(f'{d1[result - result % 10]} {d1[result % 10]}')
    else:
        print(f'{d1[result]}')


c = input('Введите знак операции ')
a = int(input('Введите 1-ое число '))
b = int(input('Введите 2-ое число '))

count = 0
while(c != 'stop'):
    culc1(a, b, c)
    c = input('Введите знак операции ')
    if c != 'stop':
        a = int(input('Введите 1-е число '))
        b = int(input('Введите 2-ое число '))
    count += 1
print(f'Выполнено {count} операций')
