import unittest
from .sd import standard_deviation
from .sd import standard_error

class MyTest(unittest.TestCase):
	def test_valid_cases(self):
		self.assertEqual(standard_deviation([0]), 0)
		self.assertEqual(standard_error([0]), 0)

		self.assertEqual(standard_deviation([1]), 0)
		self.assertEqual(standard_error([1]), 0)

		self.assertEqual(standard_deviation([0,0,0]), 0)
		self.assertEqual(standard_error([0,0,0]), 0)

		self.assertEqual(standard_deviation([1,1,1]), 0)
		self.assertEqual(standard_error([1,1,1]), 0)

		self.assertEqual(standard_deviation([0,1,2]), 0.816496580927726)
		self.assertEqual(standard_error([0,1,2]), 0.47140452079103173)

		self.assertEqual(standard_deviation([0,-1,-2]), 0.816496580927726)
		self.assertEqual(standard_error([0,-1,-2]), 0.47140452079103173)
		
		list = []
		for i in range(10000):
			list.append(i)

		self.assertEqual(standard_deviation(list), 2886.751331514372)
		self.assertEqual(standard_error(list), 28.867513315143718)
		
		list = []
		for i in range(9999999):
			list.append(i)
		
		self.assertEqual(standard_deviation(list), 2886751.0572787286)
		self.assertEqual(standard_error(list), 912.8708835335426)
		
		print("Valid Test Cases has been verified!")

	def test_error_cases(self):
		self.assertRaises(ZeroDivisionError, standard_deviation, [])
		self.assertRaises(ZeroDivisionError, standard_error, [])
		
		self.assertRaises(TypeError, standard_deviation, [""])
		self.assertRaises(TypeError, standard_error, [""])
		
		self.assertRaises(TypeError, standard_deviation, [0,""])
		self.assertRaises(TypeError, standard_error, [0,""])
		
		self.assertRaises(TypeError, standard_deviation, None)
		self.assertRaises(TypeError, standard_error, None)
		
		self.assertRaises(ZeroDivisionError, standard_deviation, "")
		self.assertRaises(ZeroDivisionError, standard_error, "")
		
		self.assertRaises(ZeroDivisionError, standard_deviation, {})
		self.assertRaises(ZeroDivisionError, standard_error, {})

my_test = MyTest()
my_test.test_valid_cases()
my_test.test_error_cases()
