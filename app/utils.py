def file2list(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines
