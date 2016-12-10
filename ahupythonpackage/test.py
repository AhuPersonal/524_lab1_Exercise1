import unittest
from ahupythonpackage import standard_deviation
from ahupythonpackage import standard_error

class MyTest(unittest.TestCase):
	def test_valid_cases_1(self):
		self.assertAlmostEqual(standard_deviation([0]), 0)
		self.assertAlmostEqual(standard_error([0]), 0)

	def test_valid_cases_2(self):
		self.assertAlmostEqual(standard_deviation([1]), 0)
		self.assertAlmostEqual(standard_error([1]), 0)

	def test_valid_cases_3(self):
		self.assertAlmostEqual(standard_deviation([0,0,0]), 0)
		self.assertAlmostEqual(standard_error([0,0,0]), 0)

	def test_valid_cases_4(self):
		self.assertAlmostEqual(standard_deviation([1,1,1]), 0)
		self.assertAlmostEqual(standard_error([1,1,1]), 0)

	def test_valid_cases_5(self):
		self.assertAlmostEqual(standard_deviation([0.0,1.0,2.0]), 0.816496580927726)
		self.assertAlmostEqual(standard_error([0.0,1.0,2.0]), 0.47140452079103173)

	def test_valid_cases_6(self):
		self.assertAlmostEqual(standard_deviation([0.0,-1.0,-2.0]), 0.816496580927726)
		self.assertAlmostEqual(standard_error([0.0,-1.0,-2.0]), 0.47140452079103173)
		
	def test_valid_cases_7(self):
		list = []
		for i in range(10000):
			list.append(i)

		self.assertAlmostEqual(standard_deviation(list), 2886.751331514372)
		self.assertAlmostEqual(standard_error(list), 28.867513315143718)
		
	def test_valid_cases_8(self):
		list = []
		for i in range(9999999):
			list.append(i)
		
		self.assertAlmostEqual(standard_deviation(list), 2886751.0572787286)
		self.assertAlmostEqual(standard_error(list), 912.8708835335426)

	def test_error_cases_1(self):
		self.assertRaises(ZeroDivisionError, standard_deviation, [])
		self.assertRaises(ZeroDivisionError, standard_error, [])
		
	def test_error_cases_2(self):
		self.assertRaises(TypeError, standard_deviation, [""])
		self.assertRaises(TypeError, standard_error, [""])
		
	def test_error_cases_3(self):
		self.assertRaises(TypeError, standard_deviation, [0,""])
		self.assertRaises(TypeError, standard_error, [0,""])
		
	def test_error_cases_4(self):
		self.assertRaises(TypeError, standard_deviation, None)
		self.assertRaises(TypeError, standard_error, None)
		
	def test_error_cases_5(self):
		self.assertRaises(ZeroDivisionError, standard_deviation, "")
		self.assertRaises(ZeroDivisionError, standard_error, "")
		
	def test_error_cases_6(self):
		self.assertRaises(ZeroDivisionError, standard_deviation, {})
		self.assertRaises(ZeroDivisionError, standard_error, {})

if __name__ == '__main__':
    unittest.main()