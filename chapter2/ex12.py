from argparse import ArgumentParser
from ex10 import get_option


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('-f', '--file', default=['popular-names.txt', 'col1.txt', 'col2.txt'], nargs=3)

    return argparser.parse_args()


def get_col(path, num):
    with open(path, "r") as f:
        rows = [r.split() for r in f.readlines()]
        col = [r[num] for r in rows]

    return col


def main():
    args = get_option()

    name = get_col(args.file[0], 0)
    sex = get_col(args.file[0], 1)

    with open(args.file[1], "w") as f:
        f.write("\n".join(name))

    with open(args.file[2], "w") as f:
        f.write("\n".join(sex))


if __name__ == "__main__":
    main()
