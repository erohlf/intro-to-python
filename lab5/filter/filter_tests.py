# Name:
# Course:
# Instructor:
# Assignment:
# Term:

import unittest
import filter


class TestCases(unittest.TestCase):

    def test_are_positive_1(self):
        list1 = [8, 6, -2]
        arepositive = filter.are_positive(list1)
        self.assertEqual(arepositive, [8, 6])
    def test_are_positive_2(self):
        list1 = [4, -9, 8]
        arepositive = filter.are_positive(list1)
        self.assertEqual(arepositive, [4, 8])

    def test_are_greater_than_n_1(self):
        list1 = [5, 9, 13]
        n = 10
        aregreater = filter.are_greater_than_n(list1, n)
        self.assertEqual(aregreater, [13])
    def test_are_greater_than_n_2(self):
        list1 = [12, 5, 6, 8, 9]
        n = 7
        aregreater = filter.are_greater_than_n(list1, n)
        self.assertEqual(aregreater, [12, 8, 9])
    
    def test_are_divisible_by_n_1(self):
        list1 = [12, 9, 7, 6]
        n = 3
        aredivisible = filter.are_divisible_by_n(list1, n)
        self.assertEqual(aredivisible, [12, 9, 6])
    def test_are_divisible_by_n_2(self):
        list1 = [8, 5, 6, 9]
        n = 2
        aredivisible = filter.are_divisible_by_n(list1, n)
        self.assertEqual(aredivisible, [8, 6])

if __name__ == '__main__':
    unittest.main()
