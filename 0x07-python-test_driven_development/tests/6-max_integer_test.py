#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_sequential_list(self):
        """Tests for the order of sequence."""
        sequential = [10, 11, 12, 13]
        self.assertEqual(max_integer(sequential), 13)

    def test_non_sequential(self):
        """Tests integers in no sequence."""
        non_sequential = [10, 11, 13, 12]
        self.assertEqual(max_integer(non_sequential), 13)

    def test_maximum_start(self):
        """Test a list with a beginning max value."""
        maximum_start = [13, 12, 11, 10]
        self.assertEqual(max_integer(maximum_start), 13)

    def test_void_list(self):
        """Tests an empty list."""
        void = []
        self.assertEqual(max_integer(void), None)

    def test_single_element_list(self):
        """Tests a single element in a list."""
        single_element = [8]
        self.assertEqual(max_integer(single_element), 8)

    def test_floats_points(self):
        """Test a list of floats."""
        floats = [2.67, 9.453, -7.454, 12.5, 16.0]
        self.assertEqual(max_integer(floats), 16.0)

    def test_integers_and_floats(self):
        """Tests for a list of integers and float points."""
        integers_and_floats = [2.78, 76.4, -8, 45, 1]
        self.assertEqual(max_integer(integers_and_floats), 76.4)

    def test_string(self):
        """Tests a string."""
        string = "John"
        self.assertEqual(max_integer(string), 'o')

    def test_list_of_strings(self):
        """Tests a list of strings."""
        strings = ["Michael", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_void_string(self):
        """Tests for a void string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
