import unittest
import conditional

class TestCases(unittest.TestCase):

   def test_max_101_1(self):
       self.assertEqual(conditional.max_101(5, 4), 5)

   def test_max_101_2(self):
       self.assertEqual(conditional.max_101(3, 7), 7)


   def test_max_of_three_1(self):
       self.assertEqual(conditional.max_of_three(2, 4, 8), 8)
   def test_max_of_three_2(self):
       self.assertEqual(conditional.max_of_three(3, 9, 4), 9)
   def test_max_of_three_3(self):
       self.assertEqual(conditional.max_of_three(3, 3, 3), 3)


   def test_rental_late_fee_1(self):
       self.assertEqual(conditional.rental_late_fee(6), 5)
   def test_rental_late_fee_2(self):
       self.assertEqual(conditional.rental_late_fee(12), 7)

if __name__ == '__main__':
   unittest.main()
