import calc

def test_summa():
    print('Тест на сложение')
    assert calc.culc1(6, 3, '+') == 9


def test_diff():
    print('Тест на вычитание')
    assert calc.culc1(6, 3, '-') == 3


def test_mult():
    print('Тест на умножение')
    assert calc.culc1(6, 3, '*') == 18

def test_d():
    print('Тест на деление')
    assert calc.culc1(6, 3, '/') == 2


test_summa()
test_diff()
test_mult()
test_d()
