"""Sonat Sweep"""


def add_window(depths, window, start=0):
    """"Return de sum of the values in a window from the starting point"""
    return sum(depths[start:window+start])


def number_of_increments(depths, window=1):
    """Return the number of increments between two consecutive elements of
       the input list considering sums of the values in a window"""
    depths = list(map(int, depths))
    increments = 0
    prev_depth = add_window(depths, window)
    for i in range(0, len(depths)):
        depth = add_window(depths, window, i)
        if prev_depth < depth:
            increments += 1
        prev_depth = depth
    return increments


if __name__ == '__main__':
    from app.utils import file2list
    inputFile = file2list("input.txt")
    print("part 1: " + str(number_of_increments(inputFile)))
    print("part 2: " + str(number_of_increments(inputFile, 3)))
    input()
