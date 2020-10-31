# Name:
# Course:
# Instructor:
# Assignment:
# Term:

import unittest
import poly

class TestPoly(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    # Example test case.
    def test_poly_add_1(self):
        poly1 = [2.3, 4.7, 1.0]
        poly2 = [1.2, 2.1, -3.2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])

    def test_poly_add_2(self):
        poly1 = [4.5, 9.2, 7.8]
        poly2 = [8.1, 6.5, 7.2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [12.6, 15.7, 15.0])

    def test_poly_mult_1(self):
        poly1 = [3, 4, 5]
        poly2 = [2, 4, 1]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [6, 20, 26, 13, 5]) 


if __name__ == '__main__':
    unittest.main()
