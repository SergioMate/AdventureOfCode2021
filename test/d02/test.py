"""Dive Test"""

import unittest
import os

from app.d02.dive import diving_planning, move_advanced
from app.utils import file2list


class TestD02(unittest.TestCase):
    """Dive Test"""
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.input_path = os.path.join(dir_path, 'input.txt')

    def test_movement(self):
        """Test the diving planning"""
        final_position=diving_planning(file2list(self.input_path))
        self.assertEqual(150, final_position.horizontal*final_position.depth)

    def test_movement_advanced(self):
        """Test the diving planning based on the advanced movement"""
        final_position=diving_planning(file2list(self.input_path), move_advanced)
        self.assertEqual(900, final_position.horizontal*final_position.depth)


if __name__ == "__main__":
    unittest.main()
