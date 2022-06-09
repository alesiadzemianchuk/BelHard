import calc

def test_summa():
    print('Тест на сложение')
    if calc.culc1(6, 3, '+') == 9:
        print('ok+\n')
    else:
        print('not ok+\n')


def test_diff():
    print('Тест на вычитание')
    if calc.culc1(6, 3, '-') == 9:
        print('ok-\n')
    else:
        print('not ok-\n')


def test_mult():
    print('Тест на умножение')
    if calc.culc1(6, 3, '*') == 18:
        print('ok*\n')
    else:
        print('not ok*\n')


def test_d():
    print('Тест на деление')
    if calc.culc1(6, 3, '/') == 9:
        print('ok/\n')
    else:
        print('not ok/\n')

test_summa()
test_diff()
test_mult()
test_d()
