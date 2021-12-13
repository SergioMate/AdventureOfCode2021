"""Sonat Sweep"""


class position:
    """Position"""
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0


def move(previousPosition, action):
    """Performs the movement action over the actual position"""
    actualPosition = previousPosition
    actionSteps = action.split()
    match actionSteps[0]:
        case 'forward':
            actualPosition.horizontal += int(actionSteps[1])
        case 'down':
            actualPosition.depth += int(actionSteps[1])
        case 'up':
            actualPosition.depth -= int(actionSteps[1])
    return actualPosition


def moveAdvanced(previousPosition, action):
    """Performs the movement action over the actual position"""
    actualPosition = previousPosition
    actionSteps = action.split()
    match actionSteps[0]:
        case 'down':
            actualPosition.aim += int(actionSteps[1])
        case 'up':
            actualPosition.aim -= int(actionSteps[1])
        case 'forward':
            actualPosition.horizontal += int(actionSteps[1])
            actualPosition.depth += actualPosition.aim * int(actionSteps[1])
    return actualPosition


def divingPlanning(actions, movement=move):
    """Return the position after the dive planning based on the movement"""
    actualPosition = position()
    for action in actions:
        actualPosition = movement(actualPosition, action)
    return actualPosition


if __name__ == '__main__':
    from app.utils import file2list
    inputFile = file2list("input.txt")
    finalPosition=divingPlanning(inputFile)
    print("part 1: " + str(finalPosition.horizontal*finalPosition.depth))
    finalPosition=divingPlanning(inputFile, moveAdvanced)
    print("part 2: " + str(finalPosition.horizontal*finalPosition.depth))
    input()
