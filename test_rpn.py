import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_add(self):
		result = rpn.calculate("1 1 + 2 +")
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate("5 2 -")
		self.assertEqual(3,result)
	def test_toomany(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate('1 2 3 +')
	def test_multiply(self):
		result = rpn.calculate('5 2 *')
		self.assertEqual(10,result)
	def test_add_subtract(self):
		result = rpn.calculate('2 3 + 1 -')
		self.assertEqual(4,result)
	def test_divide(self):
		result = rpn.calculate('10 2 /')
		self.assertEqual(5,result)
	def test_summation(self):
		result = rpn.calculate('10 2 3 5 3 S')
		self.assertEqual(23,result)
	def test_summation2(self):
		result = rpn.calculate('0 0 S')
		self.assertEqual(0, result)
	def test_factorial(self):
		result = rpn.calculate('4 !')
		self.assertEqual(24,result)
	def test_copy(self):
		result = rpn.calculate('10 2 1 5 1 C S')
		self.assertEqual(29, result)
	def test_square(self):
		result = rpn.calculate('10 2 ^')
		self.assertEqual(100, result)
	def test_cube(self):
		result = rpn.calculate('10 3 ^')
		self.assertEqual(1000, result)
