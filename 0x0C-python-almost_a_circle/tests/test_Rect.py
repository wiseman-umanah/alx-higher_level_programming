import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from io import StringIO


class RectTestCases(unittest.TestCase):
	def setUp(self):
		self.rect = Rectangle(5, 3)
		self.msg = "[Rectangle] (25) 0/0 - 5/3"
		self.result = "#####\n#####\n#####"

	def test_init1(self):
		with self.assertRaises(TypeError):
			rect1 = Rectangle("Fail", 2)
		with self.assertRaises(TypeError):
			rect1 = Rectangle(2, "Fail")
		with self.assertRaises(TypeError):
			rect1 = Rectangle(23, 10, 'Fail', 122)
		with self.assertRaises(TypeError):
			rect1 = Rectangle(23, 12, 23, 'Fail')
		
	def test_init2(self):
		with self.assertRaises(ValueError):
			rect1 = Rectangle(-1, 23)
		with self.assertRaises(ValueError):
			rect1 = Rectangle(23, 0)
		with self.assertRaises(ValueError):
			rect1 = Rectangle(23, 10, -200, 122)
		with self.assertRaises(ValueError):
			rect1 = Rectangle(23, 12, 23, -200)

	def test_width_get(self, value=None):
		if value == None:
			self.assertEqual(self.rect.width, 5)
		else:
			self.assertEqual(self.rect.width, value)
	
	def test_height_get(self, value=None):
		if value == None:
			self.assertEqual(self.rect.height, 3)
		else:
			self.assertEqual(self.rect.height, value)
	
	def test_x_get(self, value=None):
		if value == None:
			self.assertEqual(self.rect.x, 0)
		else:
			self.assertEqual(self.rect.x, value)
	
	def test_y_get(self, value=None):
		if value == None:
			self.assertEqual(self.rect.y, 0)
		else:
			self.assertEqual(self.rect.y, value)

	def test_width_set1(self):
		with self.assertRaises(TypeError):
			self.rect.width = "fail"
		with self.assertRaises(TypeError):
			self.rect.width = 2.3
		with self.assertRaises(TypeError):
			self.rect.width = [2,3]
		with self.assertRaises(TypeError):
			self.rect.width = {"fail": 2}
		with self.assertRaises(TypeError):
			self.rect.width = -2.3
		with self.assertRaises(ValueError):
			self.rect.width = -5

	def test_height_set1(self):
		with self.assertRaises(TypeError):
			self.rect.height = "fail"
		with self.assertRaises(TypeError):
			self.rect.height = 2.3
		with self.assertRaises(TypeError):
			self.rect.height = [2,3]
		with self.assertRaises(TypeError):
			self.rect.height = {"fail": 2}
		with self.assertRaises(TypeError):
			self.rect.height = -2.3
		with self.assertRaises(ValueError):
			self.rect.height = -5

	def test_x_set1(self):
		with self.assertRaises(TypeError):
			self.rect.x = "fail"
		with self.assertRaises(TypeError):
			self.rect.x = 2.3
		with self.assertRaises(TypeError):
			self.rect.x = [2,3]
		with self.assertRaises(TypeError):
			self.rect.x = {"fail": 2}
		with self.assertRaises(TypeError):
			self.rect.x = -2.3
		with self.assertRaises(ValueError):
			self.rect.x = -5

	def test_y_set1(self):
		with self.assertRaises(TypeError):
			self.rect.y = "fail"
		with self.assertRaises(TypeError):
			self.rect.y = 2.3
		with self.assertRaises(TypeError):
			self.rect.y = [2,3]
		with self.assertRaises(TypeError):
			self.rect.y = {"fail": 2}
		with self.assertRaises(TypeError):
			self.rect.y = -2.3
		with self.assertRaises(ValueError):
			self.rect.y = -5

	def test_width_set2(self):
		self.rect.width = 10
		self.test_width_get(self.rect.width)

	def test_height_set2(self):
		self.rect.height = 10
		self.test_height_get(self.rect.height)
	
	def test_x_set2(self):
		self.rect.x = 200
		self.test_x_get(self.rect.x)

	def test_y_set2(self):
		self.rect.y = 200
		self.test_y_get(self.rect.y)

	def test_area(self):
		self.assertEqual(self.rect.area(), 15)

	def test_display(self):
		with patch('sys.stdout', new_callable=StringIO) as fp:
			self.rect.display()
			IOp = fp.getvalue().strip()
		self.assertEqual(IOp, self.result)

	def test_str_rep(self):
		self.assertEqual(self.rect.__str__(), self.msg)
	
	def test_to_dict(self):
		dict = {"id": 26, "width": 5, "height": 3, "x": 0, "y": 0}
		self.assertEqual(self.rect.to_dictionary(), dict)