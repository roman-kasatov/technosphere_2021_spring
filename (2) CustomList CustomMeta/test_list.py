import unittest
# from unittest.mock import patch

from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.c_list = CustomList([1, 2, 3, 5])

    def test_ladd_custom(self):
        self.assertEqual(self.c_list + CustomList([4, 2, 6]),
                         CustomList([5, 4, 9, 5]))

    def test_ladd_custom1(self):
        self.assertEqual(CustomList([4, 2, 6]) + self.c_list,
                         CustomList([5, 4, 9, 5]))

    def test_ladd_list(self):
        self.assertEqual(self.c_list + [4, 2, 6],
                         CustomList([5, 4, 9, 5]))

    def test_radd_list(self):
        self.assertEqual([4, 2, 6] + self.c_list,
                         CustomList([5, 4, 9, 5]))

    def test_lsub_custom(self):
        self.assertEqual(self.c_list - CustomList([4, 2, 6]),
                         CustomList([-3, 0, -3, 5]))

    def test_lsub_custom1(self):
        self.assertEqual(CustomList([4, 2, 6]) - self.c_list,
                         CustomList([3, 0, 3, -5]))

    def test_lsub_list(self):
        self.assertEqual(self.c_list - [4, 2, 6],
                         CustomList([-3, 0, -3, 5]))

    def test_rsub_list(self):
        self.assertEqual([4, 2, 6] - self.c_list,
                         CustomList([3, 0, 3, -5]))

    def test_lt(self):
        self.assertEqual([3, 8] < self.c_list, 0)
        self.assertEqual([3, 5] < self.c_list, 1)

    def test_le(self):
        self.assertEqual([3, 8] <= self.c_list, 1)
        self.assertEqual([3, 10] <= self.c_list, 0)

    def test_eq(self):
        self.assertEqual([3, 8] == self.c_list, 1)
        self.assertEqual([3, 5] == self.c_list, 0)

    def test_ne(self):
        self.assertEqual([3, 8] != self.c_list, 0)
        self.assertEqual([3, 5] != self.c_list, 1)

    def test_gt(self):
        self.assertEqual([3, 8] > self.c_list, 0)
        self.assertEqual([3, 12] > self.c_list, 1)

    def test_ge(self):
        self.assertEqual([3, 8] >= self.c_list, 1)
        self.assertEqual([3, 5] >= self.c_list, 0)


if __name__ == '__main__':
    unittest.main(buffer=True)
