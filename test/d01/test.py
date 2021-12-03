"""Sonar Sweep Test"""

import unittest
import os

from app.d01.sonarsweep import number_of_increments
from app.utils import file2list


class TestD01(unittest.TestCase):
    """Sonar Sweep Test"""
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.input_path = os.path.join(dir_path, 'input.txt')

    def test_number_of_increments(self):
        """Test the number of increments without any window"""
        self.assertEqual(7, number_of_increments(file2list(self.input_path)))

    def test_number_of_increments_3(self):
        """Test the number of increments with a window of 3"""
        self.assertEqual(
            5, number_of_increments(file2list(self.input_path), 3))


if __name__ == "__main__":
    unittest.main()
