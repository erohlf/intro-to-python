import unittest
import funcs

class TestCases(unittest.TestCase):
    
 def test_f_1(self):
     self.assertEqual(funcs.f(1), 9)
 def test_f_2(self):
     self.assertEqual(funcs.f(2), 32)
     

 def test_g_1(self):
     self.assertAlmostEqual(funcs.g(1, 1), .6666666666)
 def test_g_2(self):     
     self.assertEqual(funcs.g(3, 3), 2)

 
 def test_hypotenuse_1(self):
     self.assertEqual(funcs.hypotenuse(3, 4), 5)
 def test_hypotenuse_2(self):     
     self.assertEqual(funcs.hypotenuse(5, 12), 13)


 def test_is_positive_1(self):
     self.assertTrue(funcs.is_positive(2))
 def test_is_positive_2(self):    
     self.assertFalse(funcs.is_positive(-2))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

