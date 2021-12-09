from typing import List


class Day:
    def __init__(self, file_path: str, day: int, question: str = None) -> None:
        day: int = day
        question: str = question
        answer: str = None

    def solve(self):
        raise NotImplemented("Day.solve() has not been implemented")

    @staticmethod
    def load(self) -> List[str]:
        file = os.path.join(dir_path, "data", file_name)

        with open(file) as f:
            data = [line.split("\n")[0] for line in f.readlines()]

        return data

    @property
    def solution(self) -> List[str]:
        width = 80
        lines = []

        if self.day == 1:
            lines.append("-" * width)

        lines.append("Day {}".format(self.day))

        if self.question is not None:
            lines.append("{}".format(self.question))

        if self.answer is not None:
            lines.append("Answer {}".format(self.answer))

        lines.append("-" * width)

        print("\n".join(lines))
        return lines
