"""Dive Test"""

import unittest
import os

from app.d02.dive import divingPlanning, moveAdvanced
from app.utils import file2list


class TestD02(unittest.TestCase):
    """Dive Test"""
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.input_path = os.path.join(dir_path, 'input.txt')

    def test_movement(self):
        """Test the diving planning"""
        finalPosition=divingPlanning(file2list(self.input_path))
        self.assertEqual(150, finalPosition.horizontal*finalPosition.depth)

    def test_movement_advanced(self):
        """Test the diving planning based on the advanced movement"""
        finalPosition=divingPlanning(file2list(self.input_path), moveAdvanced)
        self.assertEqual(900, finalPosition.horizontal*finalPosition.depth)


if __name__ == "__main__":
    unittest.main()
