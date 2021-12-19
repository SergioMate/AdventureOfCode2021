"""Utils"""

import io


def file2list(filename):
    """Return a list of the lines of the file"""
    with io.open(filename, 'r', encoding='utf8') as file:
        lines = file.read().splitlines()
    return lines


def bin2int(binary):
    """Binary list to integer"""
    return int(''.join(binary), 2)
