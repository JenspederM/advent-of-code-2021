import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = "{}/input.txt".format(dir_path)

if __name__ == "__main__":
    with open(file_path, "r") as f:
        measurements = [m.split("\n")[0] for m in f.readlines()]

    n = len(measurements)

    answer = sum(m1 < m2 for m1, m2 in zip(measurements[: n - 1], measurements[1:]))

    print("How many measurements are larger than the previous measurement?")
    print("--> {}".format(answer))
