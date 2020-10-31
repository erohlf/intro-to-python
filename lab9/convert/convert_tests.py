import unittest
import convert


class TestCases(unittest.TestCase):

    def test_convert_1(self):
        val = 'xyz'
        flt = 3.4
        self.assertEqual(convert.float_default(val, flt), 3.4)

    def test_convert_2(self):
        val = '7.21'
        flt = 6.1
        self.assertAlmostEqual(convert.float_default(val, flt), 7.21)


if __name__ == '__main__':
    unittest.main()

