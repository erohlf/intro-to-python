import unittest
import funcs

class TestCases(unittest.TestCase):
    
 def test_pounds_to_kg_1(self):
     self.assertAlmostEqual(funcs.pounds_to_kg(2), .9071840000)
 def test_pounds_to_kg_2(self):
     self.assertAlmostEqual(funcs.pounds_to_kg(171), 77.56423200)
    
 def test_get_mass_object_1(self):
     self.assertEqual(funcs.get_mass_object('t'), 0.1)
 def test_get_mass_object_2(self):
     self.assertEqual(funcs.get_mass_object('p'), 1.0)
 def test_get_mass_object_3(self):
     self.assertEqual(funcs.get_mass_object('r'), 3.0)
 def test_get_mass_object_4(self):
     self.assertEqual(funcs.get_mass_object('g'), 5.3)
 def test_get_mass_object_5(self):
     self.assertEqual(funcs.get_mass_object('l'), 9.07)
 def test_get_mass_object_6(self):
     self.assertEqual(funcs.get_mass_object(17), 0.0)

 def test_get_velocity_object_1(self):
     self.assertAlmostEqual(funcs.get_velocity_object(21), 10.143963722332)
 def test_get_velocity_object_2(self):
     self.assertAlmostEqual(funcs.get_velocity_object(3), 3.8340579025)

 def test_get_velocity_skater_1(self):
     self.assertAlmostEqual(funcs.get_velocity_skater(77, 5.3, 7.865), 0.54135713) 
 def test_get_velocity_skater_2(self):
     self.assertAlmostEqual(funcs.get_velocity_skater(66, 9.07, 5.27), 0.72422576)


if __name__ == '__main__':
    unittest.main()
