#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_positive_numbers(self):
        """Test with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        """Test with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative integers"""
        self.assertEqual(max_integer([-1, 0, 3, -4, 2]), 3)
        self.assertEqual(max_integer([0, -1, -2, 4, -5]), 4)

    def test_single_element(self):
        """Test with a single element in the list"""
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test with floats"""
        self.assertEqual(max_integer([1.5, 2.3, 3.1, 0.8]), 3.1)

    def test_mixed_types(self):
        """Test with a mix of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.2]), 4.2)

    def test_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertEqual(max_integer([""]), "")

    def test_none(self):
        """Test with None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_arguments(self):
        """Test when no argument is passed"""
        self.assertIsNone(max_integer())


if __name__ == "__main__":
    unittest.main()
