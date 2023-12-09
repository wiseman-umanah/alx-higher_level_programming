from models.square import Square
import unittest


class SquareTestCase(unittest.TestCase):
	def setUp(self):
		self.square = Square(5)
		self.msg = "[Square] (47) 0/0 - 5"

	def test_init1(self):
		with self.assertRaises(TypeError):
			tmp = Square("Fail", 2)
		with self.assertRaises(TypeError):
			tmp = Square(2, "Fail")
		with self.assertRaises(TypeError):
			tmp = Square(23, 122, "Fail")
		
	def test_init2(self):
		with self.assertRaises(ValueError):
			tmp = Square(-1, 23)
		with self.assertRaises(ValueError):
			tmp = Square(23, -20)
		with self.assertRaises(ValueError):
			tmp = Square(23, 10, -200)

	def test_size_get(self, value=None):
		if value == None:
			self.assertEqual(self.square.size, 5)
		else:
			self.assertEqual(self.square.size, value)

	def test_size_set1(self):
		with self.assertRaises(TypeError):
			self.square.size = "fail"
		with self.assertRaises(TypeError):
			self.square.size = 2.3
		with self.assertRaises(TypeError):
			self.square.size = [2,3]
		with self.assertRaises(TypeError):
			self.square.size = {"fail": 2}
		with self.assertRaises(TypeError):
			self.square.size = -2.3
		with self.assertRaises(ValueError):
			self.square.size = -5

	def test_size_set2(self):
		self.square.size = 10
		self.test_size_get(self.square.size)

	def test_to_dict(self):
		dict = {"id": 48, "size": 5, "x": 0, "y": 0}
		self.assertEqual(self.square.to_dictionary(), dict)

	def test_str_rep(self):
		self.assertEqual(self.square.__str__(), self.msg)