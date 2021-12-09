from utils import read_data, print_solution


def day_01():
    question = "How many measurements are larger than the previous measurement?"
    data = read_data("day_one.txt")
    n = len(data)
    answer = sum(m1 < m2 for m1, m2 in zip(data[: n - 1], data[1:]))
    print_solution(1, answer, question)
    return data
