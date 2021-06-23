import re
from ex12 import get_col


def main():
    path1 = "./col1.txt"
    path2 = "./col2.txt"
    path3 = "./col12.txt"

    col1 = get_col(path1, 0)
    col2 = get_col(path2, 0)

    col12 = [w1 + "\t" + w2 for w1, w2 in zip(col1, col2)]

    with open(path3, "w") as f:
        f.write("\n".join(col12))


if __name__ == "__main__":
    main()
