"""
Module that test the Rectangle module and its functions
"""
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from io import StringIO
import os


class RectTestCases(unittest.TestCase):
    """
    This contains all the function that are meant to
    test the Rectangle module

    Methods:
        setUp:
            The setup for creating an new Rectangle instance

        test_init:
            This test the initialization process of Rectangle instance
            with different parameters

            Functions:
                test_init1

                test_init2:

        test_width_get:
            This test the return value of the width getter

        test_height_get:
            This test the return value of the height getter

        test_x_get:
            This test the return value of the x getter

        test_y_get:
            This test the return value of the y getter

        test_width_set:
            This test the funtion of the width setter

            Functions:
                test_width_set1
                test_width_set2

        test_height_set:
            This test the funtion of the height setter

            Functions:
                test_height_set1
                test_height_set2

        test_x_set:
            This test the funtion of the x setter

            Functions:
                test_x_set1
                test_x_set2

        test_y_set:
            This test the funtion of the y setter

            Functions:
                test_y_set1
                test_y_set2

        test_area:
            Test the return value of the Rectangle area function

        test_display:
            Checks what the display function prints to the screen

        test_str_rep:
            Checks the class string representation

        test_to_dict:
            Checks the return value of the to_dictionary
            function of the Rectangle module

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
        self.rect = Rectangle(5, 3)
        self.file1 = "Rectangle.json"
        self.file2 = "Rectangle.csv"
        self.msg = "[Rectangle] (57) 0/0 - 5/3"
        self.result = "#####\n#####\n#####"

    def test_init1(self):
        """
        Checks the initialization process of Rectangle module
        """
        with self.assertRaises(TypeError):
            rect1 = Rectangle("Fail", 2)
        with self.assertRaises(TypeError):
            rect1 = Rectangle(2, "Fail")
        with self.assertRaises(TypeError):
            rect1 = Rectangle(23, 10, 'Fail', 122)
        with self.assertRaises(TypeError):
            rect1 = Rectangle(23, 12, 23, 'Fail')

    def test_init2(self):
        """
        Checks the initialization process of Rectangle module
        """
        with self.assertRaises(ValueError):
            rect1 = Rectangle(-1, 23)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(23, 0)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(23, 10, -200, 122)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(23, 12, 23, -200)
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect1.id, 5)

    def test_width_get(self, value=None):
        """
        Checks the return value of width getter
        """
        if value is None:
            self.assertEqual(self.rect.width, 5)
        else:
            self.assertEqual(self.rect.width, value)

    def test_height_get(self, value=None):
        """
        Checks the return value of height getter
        """
        if value is None:
            self.assertEqual(self.rect.height, 3)
        else:
            self.assertEqual(self.rect.height, value)

    def test_x_get(self, value=None):
        """
        Checks the return value of x getter
        """
        if value is None:
            self.assertEqual(self.rect.x, 0)
        else:
            self.assertEqual(self.rect.x, value)

    def test_y_get(self, value=None):
        """
        Checks the return value of y getter
        """
        if value is None:
            self.assertEqual(self.rect.y, 0)
        else:
            self.assertEqual(self.rect.y, value)

    def test_width_set1(self):
        """
        Sets the value of width with different parameters
        """
        with self.assertRaises(TypeError):
            self.rect.width = "fail"
        with self.assertRaises(TypeError):
            self.rect.width = 2.3
        with self.assertRaises(TypeError):
            self.rect.width = [2, 3]
        with self.assertRaises(TypeError):
            self.rect.width = {"fail": 2}
        with self.assertRaises(TypeError):
            self.rect.width = -2.3
        with self.assertRaises(ValueError):
            self.rect.width = -5

    def test_height_set1(self):
        """
        Sets the value of height with different parameters
        """
        with self.assertRaises(TypeError):
            self.rect.height = "fail"
        with self.assertRaises(TypeError):
            self.rect.height = 2.3
        with self.assertRaises(TypeError):
            self.rect.height = [2, 3]
        with self.assertRaises(TypeError):
            self.rect.height = {"fail": 2}
        with self.assertRaises(TypeError):
            self.rect.height = -2.3
        with self.assertRaises(ValueError):
            self.rect.height = -5

    def test_x_set1(self):
        """
        Sets the value of x with different parameters
        """
        with self.assertRaises(TypeError):
            self.rect.x = "fail"
        with self.assertRaises(TypeError):
            self.rect.x = 2.3
        with self.assertRaises(TypeError):
            self.rect.x = [2, 3]
        with self.assertRaises(TypeError):
            self.rect.x = {"fail": 2}
        with self.assertRaises(TypeError):
            self.rect.x = -2.3
        with self.assertRaises(ValueError):
            self.rect.x = -5

    def test_y_set1(self):
        """
        Sets the value of y with different parameters
        """
        with self.assertRaises(TypeError):
            self.rect.y = "fail"
        with self.assertRaises(TypeError):
            self.rect.y = 2.3
        with self.assertRaises(TypeError):
            self.rect.y = [2, 3]
        with self.assertRaises(TypeError):
            self.rect.y = {"fail": 2}
        with self.assertRaises(TypeError):
            self.rect.y = -2.3
        with self.assertRaises(ValueError):
            self.rect.y = -5

    def test_width_set2(self):
        """
        Sets the value of width and checks the return value
        """
        self.rect.width = 10
        self.test_width_get(self.rect.width)

    def test_height_set2(self):
        """
        Sets the value of height and checks the return value
        """
        self.rect.height = 10
        self.test_height_get(self.rect.height)

    def test_x_set2(self):
        """
        Sets the value of x and checks the return value
        """
        self.rect.x = 200
        self.test_x_get(self.rect.x)

    def test_y_set2(self):
        """
        Sets the value of y and checks the return value
        """
        self.rect.y = 200
        self.test_y_get(self.rect.y)

    def test_area(self):
        """
        Checks the return value of the area function
        """
        self.assertEqual(self.rect.area(), 15)

    def test_display(self):
        """
        Checks what will be displayed to standard output
        """
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.rect.display()
            IOp = fp.getvalue().strip()
        self.assertEqual(IOp, self.result)

    def test_display_y_none(self):
        """
        Checks what will be displayed to standard output
        without y
        """
        temp1 = Rectangle(2, 2, 2)
        with patch("sys.stdout", new_callable=StringIO) as fp:
            temp1.display()
            IOp = fp.getvalue().strip()
        self.assertEqual(IOp, "##\n  ##")

    def test_str_rep(self):
        """
        Checks the return value of the string representation of the module
        """
        self.assertEqual(self.rect.__str__(), self.msg)

    def test_to_dict(self):
        """
        Checks the return value of to_dictionary function
        """
        dict = {"id": 58, "width": 5, "height": 3, "x": 0, "y": 0}
        self.assertEqual(self.rect.to_dictionary(), dict)

    def test_save_to_file(self):
        """
        Checks if file is properly created
        """
        Rectangle.save_to_file([self.rect])
        self.assertTrue(self.file1 in os.listdir(os.getcwd()))

    def test_save_to_file_ins(self):
        """
        Checks if file is properly created
        with one parameter
        """
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(self.file1 in os.listdir(os.getcwd()))

    def test_save_to_file_None(self):
        """
        Checks if file is properly created
        With None parameter
        """
        Rectangle.save_to_file(None)
        self.assertTrue(self.file1 in os.listdir(os.getcwd()))
        self.text_check_file()

    def test_save_to_file_empty(self):
        """
        Checks if file is properly created
        With empty parameter
        """
        Rectangle.save_to_file([])
        self.assertTrue(self.file1 in os.listdir(os.getcwd()))
        self.text_check_file()

    def text_check_file(self):
        """
        Checks the instance of the content of file created
        Content must be a list
        """
        ins = Rectangle.load_from_file()
        chk = isinstance(ins, list)
        self.assertTrue(chk)

    def test_save_to_file_csv(self):
        """
        Checks if file is properly created
        """
        Rectangle.save_to_file_csv([self.rect])
        self.assertTrue(self.file2 in os.listdir(os.getcwd()))

    def test_save_to_file_mul(self):
        """
        Checks if file is properly created with more than one instance
        """
        temp1 = Rectangle(10, 5)
        temp2 = Rectangle(15, 6)
        Rectangle.save_to_file([self.rect, temp1, temp2])
        self.assertTrue(self.file1 in os.listdir(os.getcwd()))

    def text_check_file_csv(self):
        """
        Checks the instance of the content of file created
        Content must be a list
        """
        ins = Rectangle.load_from_file_csv()
        chk = True if isinstance(ins, Rectangle) else False
        self.assertTrue(chk)

    def test_save_to_file_csv(self):
        """
        Checks if file is properly created
        """
        Rectangle.save_to_file_csv([self.rect])
        self.assertTrue(self.file2 in os.listdir(os.getcwd()))

    def test_save_to_file_csv_mul(self):
        """
        Checks if file is properly created with more than one instance
        """
        temp1 = Rectangle(10, 5)
        temp2 = Rectangle(15, 3)
        Rectangle.save_to_file_csv([self.rect, temp1, temp2])
        self.assertTrue(self.file2 in os.listdir(os.getcwd()))

    def test_load_from_file(self):
        """
        Loads from a file and checks the instance
        Contents must be a list
        """
        result = self.rect.load_from_file()
        boo = isinstance(result, list)
        self.assertEqual(boo, True)

    def test_create(self):
        """
        Test if code can successfully create a new instance
        """
        tmp = self.rect.create(**{"id": 2})
        self.assertTrue(isinstance(tmp, Rectangle))
        self.assertEqual(tmp.id, 2)

    def test_create1(self):
        """
        Test if code can successfully create a new instance
        """
        tmp = self.rect.create(**{"id": 2, "width": 2})
        self.assertTrue(isinstance(tmp, Rectangle))
        self.assertEqual(tmp.width, 2)

    def test_create2(self):
        """
        Test if code can successfully create a new instance
        """
        tmp = self.rect.create(**{"id": 2, "width": 2, "height": 4})
        self.assertTrue(isinstance(tmp, Rectangle))
        self.assertEqual(tmp.height, 4)

    def test_create3(self):
        """
        Test if code can successfully create a new instance
        """
        tmp = self.rect.create(**{"id": 2, "width": 2, "height": 4, "x": 300})
        self.assertTrue(isinstance(tmp, Rectangle))
        self.assertEqual(tmp.x, 300)

    def test_create4(self):
        """
        Test if code can successfully create a new instance
        """
        tmp = self.rect.create(**{"id": 2, "width": 2, "height": 4,
                                  "x": 300, "y": 300})
        self.assertTrue(isinstance(tmp, Rectangle))
        self.assertEqual(tmp.y, 300)

    def test_update(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update()

    def test_update1(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(89)
        self.assertEqual(self.rect.id, 89)

    def test_update2(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(89, 10)
        self.test_width_get(10)

    def test_update2(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(89, 10, 15)
        self.test_height_get(15)

    def test_update3(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(89, 10, 15, 200)
        self.test_x_get(200)

    def test_update4(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(89, 10, 15, 200, 300)
        self.test_y_get(300)

    def test_update5(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(**{"id": 89})
        self.assertEqual(self.rect.id, 89)

    def test_update6(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(**{"id": 89, "width": 10})
        self.test_width_get(10)

    def test_update6(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(**{"id": 89, "width": 10, "height": 15})
        self.test_height_get(15)

    def test_update7(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(**{"id": 89, "width": 10, "height": 15, "x": 200})
        self.test_x_get(200)

    def test_update8(self):
        """
        Test the update function that updates the values of instance
        """
        self.rect.update(**{"id": 89, "width": 10, "height": 15,
                            "x": 200, "y": 300})
        self.test_y_get(300)
