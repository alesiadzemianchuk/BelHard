import calc
import unittest

class Test(unittest.TestCase):

    def test_summa(self):
        self.assertEqual(calc.culc1(6, 3, '+'), 9)

    def test_diff(self):
        self.assertEqual(calc.culc1(6, 3, '-'), 3)

    def test_mult(self):
        self.assertEqual(calc.culc1(6, 3, '*'), 18)

    def test_d(self):
        self.assertEqual(calc.culc1(6, 3, '/'), 2)



if __name__ == '__main__':
    unittest.main()


