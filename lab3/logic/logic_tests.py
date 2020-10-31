import unittest
import logic

class TestCases(unittest.TestCase):

   def test_is_even_1(self):
       self.assertTrue(logic.is_even(18))

   def test_is_even_2(self):
       self.assertFalse(logic.is_even(23))

   def test_in_an_interval_1(self):
       self.assertTrue(logic.in_an_interval(7))

   def test_in_an_interval_2(self):
       self.assertFalse(logic.in_an_interval(27))

   def test_in_an_interval_3(self):
       self.assertFalse(logic.in_an_interval(12))

if __name__ == '__main__':
   unittest.main()
