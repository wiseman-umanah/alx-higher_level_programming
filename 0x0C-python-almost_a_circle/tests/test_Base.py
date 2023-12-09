import unittest
import os
import json
from models.base import Base


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.base = Base()
    def test_to_json_string1(self):
        result = self.base.to_json_string({"id": 1, "man": "Oboy"})
        self.assertEqual(result, '{"id": 1, "man": "Oboy"}')

    def test_to_json_string2(self):
        self.assertEqual(self.base.to_json_string([]), '[]')

    def test_to_json_string3(self):
        self.assertEqual(self.base.to_json_string(None), '[]')

    def test_json_save_empty(self):
        with self.assertRaises(TypeError) as e:
            self.base.save_to_file()

    def test_json_load1(self):
        result = self.base.from_json_string('[]')
        self.assertEqual(result, [])

    def test_json_load2(self):
        self.assertEqual(self.base.from_json_string(None), '[]')

    def test_json_load3(self):
        result = self.base.from_json_string('["hello", "world"]')
        self.assertEqual(result, ["hello", "world"])

    def test_json_load4(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            self.base.from_json_string("Wrong input")

    def test_json_load5(self):
        result = self.base.from_json_string('{"id": 1, "m" : "hey"}')
        self.assertEqual(result, {"id": 1, "m": "hey"})
    