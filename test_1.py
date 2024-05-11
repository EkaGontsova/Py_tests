import unittest


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def solution(a, b, c):
    d = discriminant(a, b, c)
    if d < 0:
        return "корней нет"
    elif d == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return (x1, x2)


class TestMathMethods(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(discriminant(1, 8, 15), 4)
        self.assertEqual(discriminant(1, -13, 12), 121)
        self.assertEqual(discriminant(-4, 28, -49), 0)
        self.assertEqual(discriminant(1, 1, 1), -3)

    def test_solution(self):
        self.assertEqual(solution(1, 8, 15), (-3.0, -5.0))
        self.assertEqual(solution(1, -13, 12), (12.0, 1.0))
        self.assertEqual(solution(-4, 28, -49), (3.5,))
        self.assertEqual(solution(1, 1, 1), 'корней нет')


if __name__ == '__main__':
    unittest.main()
