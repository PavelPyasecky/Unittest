import unittest


def factorize(n):
    """
    Factorize positive integer and return its factors.
    :type n: int,>=0
    :rtype: tuple[N],N>0
    """

    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return tuple(primfac)


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for x in ["string", 1.5]:
            with self.subTest(case=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        for x in -1, -10, -100:
            with self.subTest(case=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        for x in 0, 1:
            with self.subTest(case=x):
                self.assertEqual(factorize(x), (x,))

    def test_simple_numbers(self):
        for x in 3, 13, 29:
            with self.subTest(case=x):
                self.assertEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self):
        test_cases = (
            (6, (2, 3)),
            (26, (2, 13)),
            (121, (11, 11)),
        )
        for k, expected in test_cases.items():
            with self.subTest(case=k):
                self.assertEqual(factorize(k), expected)

    def test_many_multipliers(self):
        test_cases = (
            (1001, (7, 11, 13)),
            (9699690, (2, 3, 5, 7, 11, 13, 17, 19)),
        )
        for k, expected in test_cases.items():
            with self.subTest(case=k):
                self.assertEqual(factorize(k), expected)
