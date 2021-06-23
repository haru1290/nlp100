import sys


def tail(path, n):
    with open(path, "r") as f:
        rows = f.readlines()

    return "".join(rows[-int(n):])


def main():
    path = "./popular-names.txt"

    print(tail(path, sys.argv[1]))


if __name__ == "__main__":
    main()

