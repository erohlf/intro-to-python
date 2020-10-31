# Name:
# Course:
# Instructor:
# Assignment:
# Term:

import unittest
import map


class TestCases(unittest.TestCase):

    def test_1_square_all(self):
        list1 = [3, 4, 5]
        squarelist = map.square_all(list1)
        self.assertEqual(squarelist, [9, 16, 25])
    def test_2_square_all(self):
        list1 = [6, 7, 8]
        squarelist = map.square_all(list1)
        self.assertEqual(squarelist, [36, 49, 64])

    def test_1_add_n_all(self):
        list1 = [2, 4, 7]
        n = 5
        addn = map.add_n_all(list1, n)
        self.assertEqual(addn, [7, 9, 12])
    def test_2_add_n_all(self): 
        list1 = [4, 6, 2]
        n = 8
        addn = map.add_n_all(list1, n)
        self.assertEqual(addn, [12, 14, 10])
    
    def test_1_even_or_odd_all(self):
        list1 = [8, 9, 4]
        evnodd = map.even_or_odd_all(list1)
        self.assertEqual(evnodd, [True, False, True])
    def test_2_even_or_odd_all(self):
        list1 = [1, 3, 6]
        evnodd = map.even_or_odd_all(list1)
        self.assertEqual(evnodd, [False, False, True])


if __name__ == '__main__':
    unittest.main()
