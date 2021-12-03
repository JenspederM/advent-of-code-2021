import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = "{}/input.txt".format(dir_path)

if __name__ == "__main__":
    with open(file_path, "r") as f:
        directions = [d.split("\n")[0] for d in f.readlines()]

    x = 0
    y = 0

    for line in directions:
        d, v = line.split(" ")

        if d == "forward":
            x += int(v)
        elif d == "down":
            y += int(v)
        elif d == "up":
            y -= int(v)
        else:
            raise KeyError("Direction {} is not supported".format(d))

    print("Solution:")
    print()
    print("x = {}, y = {}".format(x, y))
    print("x*y = {}".format(x * y))
