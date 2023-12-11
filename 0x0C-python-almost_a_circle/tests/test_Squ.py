from models.square import Square
import unittest
import os


class SquareTestCase(unittest.TestCase):
	def setUp(self):
		self.square = Square(5)
		self.file1 = "Square.json"
		self.file2 = "Square.csv"
		self.msg = "[Square] (57) 0/0 - 5"

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
		dict = {"id": 58, "size": 5, "x": 0, "y": 0}
		self.assertEqual(self.square.to_dictionary(), dict)

	def test_str_rep(self):
		self.assertEqual(self.square.__str__(), self.msg)

	def test_save_to_file(self):
		Square.save_to_file([self.square])
		self.assertTrue(self.file1 in os.listdir(os.getcwd()))
	
	def test_save_to_file_mul(self):
		temp1 = Square(10)
		temp2 = Square(15)
		Square.save_to_file([self.square, temp1, temp2])
		self.assertTrue(self.file1 in os.listdir(os.getcwd()))
	
	def text_check_file(self):
		ins = Square.load_from_file()
		chk = True if isinstance(ins, Square) else False
		self.assertTrue(chk)

	def test_save_to_file_csv(self):
		Square.save_to_file_csv([self.square])
		self.assertTrue(self.file2 in os.listdir(os.getcwd()))
	
	def test_save_to_file_csv_mul(self):
		temp1 = Square(10)
		temp2 = Square(15)
		Square.save_to_file([self.square, temp1, temp2])
		self.assertTrue(self.file2 in os.listdir(os.getcwd()))

	def text_check_file_csv(self):
		ins = Square.load_from_file_csv()
		chk = True if isinstance(ins, Square) else False
		self.assertTrue(chk)