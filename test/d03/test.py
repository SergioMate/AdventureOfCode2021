"""Binary Diagnostic Test"""

from app.d03.binary_diagnostic import PowerConsumption, LifeSupport
from app.utils import file2list
import os
import unittest


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

    def test_life_support(self):
        """Test the life support"""
        life_support = LifeSupport(file2list(self.input_path))
        self.assertEqual(
            230, life_support.oxygen_generator * life_support.co2_scrubber)


if __name__ == "__main__":
    unittest.main()
