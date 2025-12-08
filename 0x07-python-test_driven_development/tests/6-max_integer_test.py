#!/usr/bin/python3
"""
Unittest for max_integer([...])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            max_integer("string")
        with self.assertRaises(TypeError):
            max_integer({"key": "Value"})
        with self.assertRaises(TypeError):
            max_integer(20)
        with self.assertRaises(TypeError):
            max_integer(("tuple",))
        with self.assertRaises(TypeError):
            max_integer({"set"})
        with self.assertRaises(TypeError):
            max_integer(["string", 8, 9])
