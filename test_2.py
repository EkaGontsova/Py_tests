import unittest


def vote(votes):
    d = {}
    for v in votes:
        d.setdefault(v, 0)
        d[v] += 1
    sorted_by_count = sorted(d.items(), key=lambda a: a[1], reverse=True)
    return sorted_by_count[0][0]


class Test(unittest.TestCase):
    def test_single_winner(self):
        self.assertEqual(vote([1, 1, 1, 2, 3]), 1)

    def test_multiple_winners(self):
        self.assertEqual(vote([1, 2, 3, 2, 2]), 2)

    def test_no_votes(self):
        with self.assertRaises(IndexError):
            vote([])


if __name__ == '__main__':
    unittest.main()
