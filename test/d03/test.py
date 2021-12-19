"""Binary Diagnostic Test"""

import unittest
import os

from app.d03.binary_diagnostic import PowerConsumption
from app.utils import file2list


class TestD03(unittest.TestCase):
    """Binary Diagnostic Test"""
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.input_path = os.path.join(dir_path, 'input.txt')

    def test_power_consumption(self):
        """Test the power consumption"""
        power_consumption = PowerConsumption(file2list(self.input_path))
        self.assertEqual(
            198, power_consumption.gamma * power_consumption.epsilon)


if __name__ == "__main__":
    unittest.main()
