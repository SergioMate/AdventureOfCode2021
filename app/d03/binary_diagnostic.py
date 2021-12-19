"""Binary Diagnostic"""
import statistics
from app.utils import bin2int


class PowerConsumption:
    """PowerConsumption"""
    def __init__(self, binary_codes):
        self._gamma = extract_gamma(binary_codes)
        self._epsilon = self.extract_epsilon(binary_codes)

    def extract_epsilon(self, binary_codes):
        """Return epsilon rate"""
        return ~self.gamma & bin2int(["1"] * len(binary_codes[0]))

    @property
    def gamma(self):
        """gamma property getter"""
        return self._gamma

    @property
    def epsilon(self):
        """epsilon property getter"""
        return self._epsilon


def extract_gamma(binary_codes):
    """Return gamma rate"""
    bin_gamma = []
    for indx in range(0, len(binary_codes[0])):
        bin_gamma.append(statistics.mode(list(zip(*binary_codes))[indx]))
    return bin2int(bin_gamma)

if __name__ == '__main__':
    from app.utils import file2list
    inputFile = file2list("input.txt")
    power_consuption = PowerConsumption(inputFile)
    print("part 1: " + str(power_consuption.gamma * power_consuption.epsilon))
    input()
