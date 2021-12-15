import os
from typing import List, Union

dir_path = os.path.dirname(os.path.realpath(__file__))


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def read_data(file_name: str) -> List[str]:
    file = os.path.join(dir_path, "data", file_name)

    with open(file) as f:
        data = [line.split("\n")[0] for line in f.readlines()]

    return data


def print_solution(
    day: Union[int, str], answer: str, question: str = None, width: int = 80
) -> str:
    lines = []

    if day == 1:
        lines.append("-" * width)

    lines.append("Day {}".format(day))

    if question is not None:
        lines.append("{}".format(question))

    lines.append("= {}".format(answer))

    lines.append("-" * width)

    print("\n".join(lines))
    return lines


def most_common_byte(byte_strings: str, verbose=False) -> int:

    # Prep

    for s in byte_strings:
        bytes = [int(byte) for byte in s.split("")]

    if verbose:
        print("\n".join(bytes))

    return bytes
