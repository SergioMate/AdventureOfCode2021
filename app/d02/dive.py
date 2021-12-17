"""Sonat Sweep"""


class Position(object):
    """Position"""
    def __init__(self, _horizontal_ini=0, _depth_ini=0, _aim_ini=0):
        self._horizontal = _horizontal_ini
        self._depth = _depth_ini
        self._aim = _aim_ini

    @property
    def horizontal(self):
        return self._horizontal

    @horizontal.setter
    def horizontal(self, value):
        self._horizontal = value

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value

    @property
    def aim(self):
        return self._aim

    @aim.setter
    def aim(self, value):
        self._aim = value


def move(previous_position, action):
    """Performs the movement action over the actual position"""
    actual_position = previous_position
    actionSteps = action.split()
    match actionSteps[0]:
        case 'forward':
            actual_position.horizontal += int(actionSteps[1])
        case 'down':
            actual_position.depth += int(actionSteps[1])
        case 'up':
            actual_position.depth -= int(actionSteps[1])
    return actual_position


def move_advanced(previous_position, action):
    """Performs the movement action over the actual position"""
    actual_position = previous_position
    actionSteps = action.split()
    match actionSteps[0]:
        case 'down':
            actual_position.aim += int(actionSteps[1])
        case 'up':
            actual_position.aim -= int(actionSteps[1])
        case 'forward':
            actual_position.horizontal += int(actionSteps[1])
            actual_position.depth += actual_position.aim * int(actionSteps[1])
    return actual_position


def diving_planning(actions, movement=move):
    """Return the position after the dive planning based on the movement"""
    actual_position = Position()
    for action in actions:
        actual_position = movement(actual_position, action)
    return actual_position


if __name__ == '__main__':
    from app.utils import file2list
    inputFile = file2list("input.txt")
    final_position = diving_planning(inputFile)
    print("part 1: " + str(final_position.horizontal*final_position.depth))
    final_position = diving_planning(inputFile, move_advanced)
    print("part 2: " + str(final_position.horizontal*final_position.depth))
    input()
