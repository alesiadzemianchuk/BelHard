from num2words import num2words

def culc1(a, b, c):
    if c == '+':
        result = a + b
        print(result)
        print(num2words(result, lang='ru'))
    elif c == '-':
        result = a - b
        print(result)
        print(num2words(result, lang='ru'))
    elif c == '*':
        result = a * b
        print(result)
        print(num2words(result, lang='ru'))
    else:
        result = 0
        try:
            result = a / b
        except ZeroDivisionError:
            print('нельзя делить на ноль')
        print(result)
        print(num2words(result, lang='ru'))



c = input('Введите знак операции + - * / ')
a = int(input('Введите 1-ое число '))
b = int(input('Введите 2-ое число '))

count = 0
while(c != 'stop'):
    culc1(a, b, c)
    c = input('Введите знак операции + - * / либо stop ')
    if c != 'stop':
        a = int(input('Введите 1-е число '))
        b = int(input('Введите 2-ое число '))
    count += 1
print(f'Выполнено {count} операций')
