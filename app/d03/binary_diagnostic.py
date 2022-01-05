"""Binary Diagnostic"""
import statistics
from app.utils import bin2int


class PowerConsumption:
    """PowerConsumption"""
    def __init__(self, binary_codes):
        self._binary_codes = binary_codes
        self._gamma = self.extract_gamma()
        self._epsilon = self.extract_epsilon()
    
    def extract_gamma(self):
        """Return gamma rate"""
        bin_gamma = []
        for indx in range(0, len(self._binary_codes[0])):
            bin_gamma.append(statistics.mode(list(zip(*self._binary_codes))[indx]))
        return bin2int(bin_gamma)

    def extract_epsilon(self):
        """Return epsilon rate"""
        return ~self.gamma & bin2int(["1"] * len(self._binary_codes[0]))

    @property
    def gamma(self):
        """gamma property getter"""
        return self._gamma

    @property
    def epsilon(self):
        """epsilon property getter"""
        return self._epsilon


if __name__ == '__main__':
    from app.utils import file2list
    inputFile = file2list("input.txt")
    power_consuption = PowerConsumption(inputFile)
    print("part 1: " + str(power_consuption.gamma * power_consuption.epsilon))
    input()
