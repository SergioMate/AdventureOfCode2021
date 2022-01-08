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

    def test_bingo_winner(self):
        """Test the bingo winner"""
        bingo = Bingo(file2list(self.input_path))
        self.assertEqual(4512, bingo.winner_score)

    def test_bingo_loser(self):
        """Test the bingo looser"""
        bingo = Bingo(file2list(self.input_path))
        self.assertEqual(1924, bingo.loser_score)


if __name__ == "__main__":
    unittest.main()
