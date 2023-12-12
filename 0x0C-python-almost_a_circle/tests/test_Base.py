"""
Module that test the function of the Base module
"""
import unittest
import json
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """
    This contains all the function that are meant to
    test the Base module

    Methods:
        setUp:
            The setup for creating an new Base instance

        test_to_json_string:
            test the to_json_string function with different parameters

            Functions:
                test_to_json_string1

                test_to_json_string2

                test_to_json_string3

        test_json_save_empty:
            tests save_to_file function with no parameter

        test_json_load:
            tests the from_json_string function

            Functions:
                test_json_load1

                test_json_load2

                test_json_load3

                test_json_load4

                test_json_load5
        """
    def setUp(self):
        """
        Function to set up a new instance
        """
        self.base = Base()

    def test_id_init1(self):
        temp1 = Base(89)
        self.assertEqual(temp1.id, 89)

    def test_id_init2(self):
        temp1 = Base()
        temp1.id = 45
        self.assertEqual(temp1.id, 45)

    def test_to_json_string1(self):
        """
        Tests if to_json_string function
        correctly convert an instance to a json string
        """
        result = self.base.to_json_string({"id": 1, "man": "Oboy"})
        self.assertEqual(result, '{"id": 1, "man": "Oboy"}')

    def test_to_json_string2(self):
        """
        Tests if to_json_string function
        correctly convert an instance to a json string
        """
        self.assertEqual(self.base.to_json_string([]), '[]')

    def test_to_json_string3(self):
        """
        Tests if to_json_string function
        correctly convert an instance to a json string
        """
        self.assertEqual(self.base.to_json_string(None), '[]')

    def test_json_save_empty(self):
        """
        Tests function if an empty paramter is passed
        """
        with self.assertRaises(TypeError) as e:
            self.base.save_to_file()

    def test_json_load1(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        result = self.base.from_json_string('[]')
        self.assertEqual(result, [])

    def test_json_load2(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        self.assertEqual(self.base.from_json_string(None), '[]')

    def test_json_load3(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        result = self.base.from_json_string('["hello", "world"]')
        self.assertEqual(result, ["hello", "world"])

    def test_json_load4(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        with self.assertRaises(json.decoder.JSONDecodeError):
            self.base.from_json_string("Wrong input")

    def test_json_load5(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        result = self.base.from_json_string('{"id": 1, "m" : "hey"}')
        self.assertEqual(result, {"id": 1, "m": "hey"})
