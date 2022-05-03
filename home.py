
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#for i in a:
#    if i < 5:
#        print(i)

#a1 = [1, 1, 2, 3, 5, 8, 13, 237, 21, 34, 55, 89]
#for i in a1:
#    if i == 237:
#        break
#    elif i % 2 == 0:
#        print(i)


#a2 = 'ротошЛОшгозОШОугаозтсОДОцхцщоЬзшпр'
#a3 = ''
#for i in a2:
#    if not i.isupper():
#        a3 += i
#print(a3)


#a4 = ['alesia', 'nik', 'master']
#b = input('Введите ник ')
#while b not in a4:
#    print('Неверный ник, вводи снова')
#    b = input()
#else:
#    print(f'привет, {b}')



#c1 = int(input('Введите целое число '))
#c2 = []
#for i in range(2, c1+1):
#    if (c1 % i == 0):
#        c2.append(i)
#        print(c2)
#        break

d1 = int(input('Введите число '))
count = 1
while(d1//10) > 0:
    count += 1
    d1 = d1 /10
print(count)


for i in range(1, 51):
    if (i % 3 != 0) and (i % 2 != 0):
        print(i)

