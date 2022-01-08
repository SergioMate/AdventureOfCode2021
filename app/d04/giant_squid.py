"""Giant Squid"""


class Cell:
    """Board Cell"""
    def __init__(self, _value_ini):
        self._value = _value_ini
        self._is_marked = False

    @property
    def value(self):
        """Value of the cell"""
        return self._value

    @property
    def is_marked(self):
        """Is the cell marked"""
        return self._is_marked

    def mark(self):
        """Mark the cell"""
        self._is_marked = True


class Board:
    """Bingo Board"""
    def __init__(self, _numbers_ini):
        self._board = [[Cell(num) for num in row] for row in _numbers_ini]

    def check(self, number):
        """Checks whether number in board and mark if it is"""
        for row in self._board:
            for cell in row:
                if cell.value == number:
                    cell.mark()

    def is_winner(self):
        """Checks if board is winner"""
        return any(all(cell.is_marked for cell in row)
                   for row in self._board) \
            or any(all(cell.is_marked for cell in row)
                   for row in list(zip(*self._board)))

    @property
    def unmarked(self):
        """Gets unmarked numbers of board"""
        return [int(cell.value) for row in self._board for cell in row
                if not cell.is_marked]


class Drum:
    """Bingo Drum"""
    def __init__(self, _numbers_ini):
        self._drum = _numbers_ini
        self._actual_index = -1

    def has_next(self):
        """Checks if drum has next number"""
        return self._actual_index + 1 < len(self._drum)

    def next(self):
        """Gets next number"""
        self._actual_index += 1
        return self.actual

    @property
    def actual(self):
        """Gets actual number"""
        return self._drum[self._actual_index]


class Bingo:
    """Bingo"""
    def __init__(self, _bingo_board):
        self._drum = Drum(list(map(int, _bingo_board[0].split(","))))
        self._boards = extract_boards(_bingo_board[1:])
        self._win_scores = []
        self.play()

    def play(self):
        """Play bingo"""
        remaining_boards = self._boards.copy()
        while len(self._win_scores) < len(self._boards) \
                and self._drum.has_next():
            actual = self._drum.next()
            for board in remaining_boards:
                board.check(actual)
                if board.is_winner():
                    self._win_scores.append(sum(board.unmarked) * actual)
            remaining_boards = [brd for brd in remaining_boards
                                if not brd.is_winner()]

    @property
    def drum(self):
        """Gets bingo's drum"""
        return self._drum

    @property
    def winner_score(self):
        """Gets bingo's winner score"""
        return self._win_scores[0]

    @property
    def loser_score(self):
        """Gets bingo's loser score"""
        return self._win_scores[len(self._boards) - 1]


def extract_boards(_bingo_boards):
    """Parses boards"""
    _raw_boards = []
    for row in _bingo_boards:
        if row:
            _raw_boards[len(_raw_boards) - 1].append(
                list(map(int, row.split())))
        else:
            _raw_boards.append([])
    return list(map(Board, _raw_boards))


if __name__ == '__main__':
    from app.utils import file2list
    inputFile = file2list("input.txt")
    bingo = Bingo(inputFile)
    print("part 1: " + str(bingo.winner_score))
    print("part 2: " + str(bingo.loser_score))
    input()
