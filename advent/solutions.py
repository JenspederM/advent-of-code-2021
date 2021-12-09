from typing import List, Union
from utils import read_data, print_solution, bcolors
from pprint import pprint


def day_01(verbose=False):
    question = "How many measurements are larger than the previous measurement?"
    data = read_data("day_01.txt")

    answer = sum(m1 < m2 for m1, m2 in zip(data[: len(data) - 1], data[1:]))

    if verbose is True:
        print_solution(1, answer, question)

    return data


def day_02(verbose=False):
    question = "What do you get if you multiply your final horizontal position by your final depth?"
    data = read_data("day_02.txt")

    x = 0
    y = 0

    for line in data:
        d, v = line.split(" ")

        if d == "forward":
            x += int(v)
        elif d == "down":
            y += int(v)
        elif d == "up":
            y -= int(v)
        else:
            raise KeyError("Direction {} is not supported".format(d))

    answer = x * y

    if verbose is True:
        print_solution(
            2, "horizontal position * final depth = {}".format(answer), question
        )

    return data


def day_03(verbose=False):

    """
    Test

    00100
    """
    question = "What is the power consumption of the submarine?"
    data = read_data("day_03.txt")
    nrows = len(data)
    ncols = len(data[0])

    counts = [0 for _ in range(ncols)]

    for line in data:
        for i, byte in enumerate(line):
            counts[i] += int(byte)

    condition = nrows / 2
    gamma_rate = int("".join([str(int(count > condition)) for count in counts]), 2)
    epsilon_rate = int("".join([str(int(count < condition)) for count in counts]), 2)

    answer = gamma_rate * epsilon_rate
    if verbose:
        print_solution(
            day=3, answer="power comsumption is {}".format(answer), question=question
        )


def day_04():
    class Board:
        def __init__(self, board: List[str]) -> None:
            assert isinstance(board, list)
            self.mark_color = bcolors.WARNING
            self.last_mark = None

            nrows = len(board)
            ncols = len(board[0])

            assert nrows == ncols, "Board is not symmetrical"

            self.nrows = nrows
            self.ncols = ncols
            self.board = board

        def __repr__(self):
            rows = "\n".join([" ".join([str(c) for c in row]) for row in self.board])
            return "Board(\n{}\n)".format(rows)

        def get_row(self, index: int) -> List[str]:
            return self.board[index]

        def get_col(self, index: int) -> List[str]:
            return [row[index] for row in self.board]

        def solution(self) -> int:
            total = 0
            for row in self.board:
                for v in row:
                    if not v.startswith(self.mark_color):
                        total += int(v)
            return total * int(self.last_mark)

        @property
        def winner(self) -> bool:
            for i in range(self.nrows):
                if all(v.startswith(self.mark_color) for v in self.get_row(i)):
                    return True

            for i in range(self.ncols):
                if all(v.startswith(self.mark_color) for v in self.get_col(i)):
                    return True

            return False

        def mark(self, mark: Union[str, int]) -> None:
            if isinstance(mark, int):
                mark = str(mark)

            self.last_mark = mark

            for i in range(self.nrows):
                for j in range(self.ncols):
                    if self.board[i][j] == mark:
                        self.board[i][j] = self._make_bold(self.board[i][j])

        def _make_bold(self, value: str):
            return self.mark_color + str(value) + bcolors.ENDC

    question = "What will your final score be if you choose that board?"
    data = read_data("day_04.txt")
    marks = [c for c in data.pop(0).split(",")]
    boards = []
    winner = None

    for i, line in enumerate(data):
        if i == 0 and line == "":
            board = []
        elif line == "":
            boards.append(Board(board))
            board = []
        else:
            row = [c for c in line.split(" ") if c != ""]
            board.append(row)

    for mark in marks:
        done = False
        for board in boards:
            board.mark(mark)
            if board.winner:
                winner = board
                done = True
                break
        if done:
            break

    answer = board.solution()

    if winner:
        print_solution(4, "Final score is {}".format(answer), question)


def day_05(verbose: bool = False):
    class Board:
        def __init__(self, starts, ends) -> None:
            x_min = min(v[0] for v in starts + ends)
            x_max = max(v[0] for v in starts + ends)
            y_min = min(v[1] for v in starts + ends)
            y_max = max(v[1] for v in starts + ends)

            self.board = [
                [0 for i in range(x_min, x_max + 1)] for j in range(y_min, y_max + 1)
            ]

            for start, end in zip(starts, ends):
                self.draw_line(start, end)

        def draw_line(self, start, end):
            x1, y1 = start
            x2, y2 = end
            if x1 == x2:
                for i in range(y1, y2 + 1):
                    self.board[i][x1] += 1
            else:
                for i in range(x1, x2 + 1):
                    self.board[y1][i] += 1
            # print(str(self))

        def __str__(self) -> str:
            rows = [
                " ".join(["." if int(i) < 1 else str(i) for i in row])
                for row in self.board
            ]
            return "\n".join(rows)

    question = "how many points do at least two lines overlap?"
    data = read_data("day_05.txt")
    test = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split(
        "\n"
    )

    def parse(data):
        starts = []
        ends = []

        for line in data:
            start, end = [
                [int(v) for v in pair.split(",")] for pair in line.split(" -> ")
            ]
            starts.append(start)
            ends.append(end)

        return starts, ends

    starts, ends = parse(data)

    def get_board(starts, ends):
        x_max = max(v[0] for v in starts + ends)
        y_max = max(v[1] for v in starts + ends)
        board = [[0 for i in range(0, x_max + 1)] for j in range(0, y_max + 1)]
        return board

    board = get_board(starts, ends)

    def draw_lines(starts, ends, board):
        for start, end in zip(starts, ends):
            x1, y1 = start
            x2, y2 = end
            x_delta = abs(x1 - x2)
            y_delta = abs(y1 - y2)
            if x1 == x2 or y1 == y2:
                for x in range(min(x1, x2), min(x1, x2) + x_delta + 1):
                    for y in range(min(y1, y2), min(y1, y2) + y_delta + 1):
                        board[y][x] += 1

        return board

    board = draw_lines(starts, ends, board)

    answer = len([v for row in board for v in row if v >= 2])
    # p1(starts[0], ends[0])
    if verbose:
        print(
            "\n".join(
                ["".join(["." if v < 1 else str(v) for v in row]) for row in board]
            )
        )

    print_solution(5, "{} lines overlap at least twice".format(answer), question)

    return answer


def day_06(verbose: Union[int, bool] = 1):
    class LanternFish:
        def __init__(self, time: int = 8) -> None:
            self.time = time

        def __repr__(self) -> str:
            return str(self.time)

        def tick(self):
            self.time -= 1

        def reset(self):
            self.time = 6

    verbose = int(verbose)

    question = "How many lanternfish would there be after 80 days?"
    data = read_data("day_06.txt")
    data = [LanternFish(int(d)) for d in data[0].split(",")]
    test = [LanternFish(int(d)) for d in "3,4,3,1,2".split(",")]

    if verbose > 2:
        print("Initial state: {}".format(data))
    for day in range(1, 81):
        new_fish = []

        for fish in data:
            if fish.time == 0:
                fish.reset()
                new_fish.append(LanternFish())
            else:
                fish.tick()

        data.extend(new_fish)

        if verbose > 1:
            if day == 1:
                print("After {} day: {}".format(day, data))
            else:
                print("After {} days: {}".format(day, data))

    if verbose == 1:
        print_solution(
            6, "After 80 days, there are {} laternfish".format(len(data)), question
        )

    return len(data)


def day_07():
    question = "How much fuel must they spend to align to that position?"
    data = read_data("day_07.txt")
    data = [int(d) for d in data[0].split(",")]
    data_min = min(data)
    data_max = max(data)
    positions = {}

    for i in range(data_min, data_max):
        fuel = 0

        for d in data:
            fuel += abs(d - i)

        positions[i] = fuel

    print_solution(
        7,
        "Minimum amount of fuel: {}".format(min(positions.values())),
        question,
    )

    print()


if __name__ == "__main__":
    day_05()