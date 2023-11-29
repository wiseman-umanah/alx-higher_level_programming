#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Suite test for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([8, -7, 100, 3]), 100)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_float_numbers(self):
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-12, -8, -2, -1]), -1)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_one_number(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, 'alx'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (45, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)