"""
Module that test the Square module and its functions
"""
from models.square import Square
import unittest
import os


class SquareTestCase(unittest.TestCase):
    """
    This contains all the function that are meant to
    test the Square module

    Methods:
        setUp:
            The setup for creating an new Square instance

        test_init:
            This test the initialization process of Square instance
            with different parameters

            Functions:
                test_init1

                test_init2:

        test_size_get:
            This test the return value of the size getter

        test_size_set:
            This test the funtion of the size setter

            Functions:
                test_size_set1
                test_size_set2

        test_str_rep:
            Checks the class string representation

        test_to_dict:
            Checks the return value of the to_dictionary
            function of the Square module

        test_save_to_file:
            Checks if json file is successfully created by the function

        test_save_to_file_mul:
            Checks if json file is successfully created by the function
            with multiple instances

        test_save_to_file_csv:
            Checks if csv file is successfully created by the function

        test_save_to_file_csv_mul:
            Checks if csv file is successfully created by the function
            with multiple instances
        """
    def setUp(self):
        """
        Function to set up a new instance
        """
        self.square = Square(5)
        self.file1 = "Square.json"
        self.file2 = "Square.csv"
        self.msg = "[Square] (63) 0/0 - 5"

    def test_init1(self):
        """
        Checks the initialization process of Square module
        """
        with self.assertRaises(TypeError):
            tmp = Square("Fail", 2)
        with self.assertRaises(TypeError):
            tmp = Square(2, "Fail")
        with self.assertRaises(TypeError):
            tmp = Square(23, 122, "Fail")

    def test_init2(self):
        """
        Checks the initialization process of Square module
        """
        with self.assertRaises(ValueError):
            tmp = Square(-1, 23)
        with self.assertRaises(ValueError):
            tmp = Square(23, -20)
        with self.assertRaises(ValueError):
            tmp = Square(23, 10, -200)

    def test_size_get(self, value=None):
        """
        Checks the return value of size getter
        """
        if value is None:
            self.assertEqual(self.square.size, 5)
        else:
            self.assertEqual(self.square.size, value)

    def test_size_set1(self):
        """
        Sets the value of size with different parameters
        """
        with self.assertRaises(TypeError):
            self.square.size = "fail"
        with self.assertRaises(TypeError):
            self.square.size = 2.3
        with self.assertRaises(TypeError):
            self.square.size = [2, 3]
        with self.assertRaises(TypeError):
            self.square.size = {"fail": 2}
        with self.assertRaises(TypeError):
            self.square.size = -2.3
        with self.assertRaises(ValueError):
            self.square.size = -5

    def test_size_set2(self):
        """
        Sets the value of size and checks the return value
        """
        self.square.size = 10
        self.test_size_get(self.square.size)

    def test_to_dict(self):
        """
        Checks the return value of to_dictionary function
        """
        dict = {"id": 64, "size": 5, "x": 0, "y": 0}
        self.assertEqual(self.square.to_dictionary(), dict)

    def test_str_rep(self):
        """
        Checks the return value of the string representation of the module
        """
        self.assertEqual(self.square.__str__(), self.msg)

    def test_save_to_file(self):
        """
        Checks if file is properly created
        """
        Square.save_to_file([self.square])
        self.assertTrue(self.file1 in os.listdir(os.getcwd()))

    def test_save_to_file_mul(self):
        """
        Checks if file is properly created with more than one instance
        """
        temp1 = Square(10)
        temp2 = Square(15)
        Square.save_to_file([self.square, temp1, temp2])
        self.assertTrue(self.file1 in os.listdir(os.getcwd()))

    def text_check_file(self):
        """
        Checks the instance of the content of file created
        Content must be a list
        """
        ins = Square.load_from_file()
        chk = True if isinstance(ins, Square) else False
        self.assertTrue(chk)

    def test_save_to_file_csv(self):
        """
        Checks if file is properly created
        """
        Square.save_to_file_csv([self.square])
        self.assertTrue(self.file2 in os.listdir(os.getcwd()))

    def test_save_to_file_csv_mul(self):
        """
        Checks if file is properly created with more than one instance
        """
        temp1 = Square(10)
        temp2 = Square(15)
        Square.save_to_file_csv([self.square, temp1, temp2])
        self.assertTrue(self.file2 in os.listdir(os.getcwd()))

    def text_check_file_csv(self):
        """
        Checks the instance of the content of file created
        Content must be a list
        """
        ins = Square.load_from_file_csv()
        chk = True if isinstance(ins, Square) else False
        self.assertTrue(chk)
