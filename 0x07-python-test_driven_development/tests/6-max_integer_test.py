#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Suite test for max_integer function"""

    def test_wrongParameter(self):
        result = "hello"
        self.assertEqual(max_integer(result), "o")

    def test_wrongArg(self):
        result = [2, 3, "H", 4, 3]
        with self.assertRaises(TypeError):
            max_integer(result)

    def test_forFloat(self):
        result = [1, 2, 30.7, 4, 8, 10]
        self.assertEqual(max_integer(result), 30.7)

    def test_integers(self):
        result = [2, 8, 2, 4, 3]
        self.assertEqual(max_integer(result), 8)

    def test_emptyList(self):
        self.assertEqual(max_integer([]), None)

    def test_oneElement(self):
        self.assertEqual(max_integer([4]), 8)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)


if __name__ == '__main__':
    unittest.main()
