"""Binary Diagnostic"""
from app.utils import bin2int
import statistics


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
            bin_gamma.append(
                statistics.mode(list(zip(*self._binary_codes))[indx]))
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


class LifeSupport:
    """LifeSupport"""
    def __init__(self, binary_codes):
        self._binary_codes = binary_codes
        self._oxygen_generator = self.extract_oxygen_generator()
        self._co2_scrubber = self.extract_co2_scrubber()

    def extract_oxygen_generator(self):
        """Return oxygen generator rate"""
        return self.extract_generic(lambda x: x)

    def extract_co2_scrubber(self):
        """Return co2 scrubber rate"""
        return self.extract_generic(lambda x:~x & 1)

    def extract_generic(self, function):
        """Iterates over binary_codes applying function filter until it gets
        last value"""
        binary_codes = self._binary_codes.copy()
        for indx in range(0, len(self._binary_codes[0])):
            bit_criteria = function(mode(binary_codes, indx))
            bit_filter = lambda code: int(code[indx]) == bit_criteria
            binary_codes = list(filter(bit_filter, binary_codes))
            if len(binary_codes) == 1:
                break
        return bin2int(binary_codes[0])

    @property
    def oxygen_generator(self):
        """oxygen generator property getter"""
        return self._oxygen_generator

    @property
    def co2_scrubber(self):
        """co2 scrubber property getter"""
        return self._co2_scrubber


def mode(binary_codes, indx):
    """Return the most common value in an index if is unique or 1 if
    several values coincide"""
    _mode = 1
    multimode = statistics.multimode(list(zip(*binary_codes))[indx])
    if len(multimode) == 1:
        _mode = int(multimode[0])
    return _mode


if __name__ == '__main__':
    from app.utils import file2list
    inputFile = file2list("input.txt")
    power_consuption = PowerConsumption(inputFile)
    print("part 1: " + str(power_consuption.gamma * power_consuption.epsilon))
    life_support = LifeSupport(inputFile)
    print("part 2: " + str(
        life_support.oxygen_generator * life_support.co2_scrubber))
    input()
