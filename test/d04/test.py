"""Giant Squid Test"""

import unittest
import os

from app.d04.giant_squid import Bingo
from app.utils import file2list


class TestD04(unittest.TestCase):
    """Giant Squid Test"""
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.input_path = os.path.join(dir_path, 'input.txt')

    def test_bingo(self):
        """Test the bingo"""
        bingo = Bingo(file2list(self.input_path))
        self.assertEqual(
            4512, sum(bingo.winner.unmarked) * bingo.drum.actual)


if __name__ == "__main__":
    unittest.main()
