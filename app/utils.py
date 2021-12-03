"""Utils"""

import io

# Return a list of the lines of the file
def file2list(filename):
    """Return a list of the lines of the file"""
    with io.open(filename, 'r', encoding='utf8') as file:
        lines = file.read().splitlines()
    return lines
