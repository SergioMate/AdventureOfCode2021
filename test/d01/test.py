"""Sonat Sweep Test"""

import unittest
import pytest
import os

from app.d01.sonarsweep import number_of_increments
from app.utils import file2list

@pytest.mark.unit
class TestD01(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.input_path = os.path.join(dir_path, 'input.txt')

    def test_number_of_increments(self):
        self.assertEqual(7, number_of_increments(file2list(self.input_path)))

    def test_number_of_increments_3(self):
        self.assertEqual(5, number_of_increments(file2list(self.input_path), 3))

if __name__ == "__main__":
    unittest.main()
    