user = 'Alesia'
age = 35
skills = ['python', 'sql', 'linux']
a, b, c = 1, 2, 3
a, b = b, a
print(a, b, c)
year = input('В каком году ты родился ')
if int(year) < 2023:
    print(f'Тебе {abs(int(year)-2022)} лет')
bool_var = True
print(bool_var)
print(int(bool_var))
float_var = 3.1415
complex_var = complex(2, 5)
print(float_var,"\n",complex_var)
print(type(float_var), type(skills))
print(isinstance(complex_var, int))
var = None
print(var is None)
print(bool(var))
print(int(float_var))
print(round(1.4), round(2.5), round(-5.35, 1))
str1 = 'Hello'
print(f"Мое имя {user}")
print(str1+", "+user)
print(f"Мое имя {user}\n" * 3)
print(skills[1])
print(str1[3:])
print(f"Мое имя {user[0]} {user[1]} {user[2]} {user[3]} {user[4]} {user[5]}")
str2 = 'Это просто длинная строка, которая нужна для тестирования'
print(str2[35:40], str2[-38:-32] )
if len(str2) > 100:
    print('Слишком длинная строка')
else:
    print(f'Строка содержит {len(str2)} символов')
print(f'{float_var:.2f}')
print(f'{user:*^10}')
print(f'{1000:+}')
numbers = 'one, two, three'
num1 = numbers.split(',')
print(num1)
print(f'{", ".join(num1)}')
print(numbers.find('two'))
print(numbers.replace('one', 'two'))
print(numbers.islower())
print(numbers.center(40, '*'))
print(str2.encode())

