from argparse import ArgumentParser
from ex12 import get_col


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('-f', '--file', default=['col1.txt', 'col2.txt', 'col12.txt'], nargs=3)

    return argparser.parse_args()


def main():
    args = get_option()

    name = get_col(args.file[0], 0)
    sex = get_col(args.file[1], 0)

    merge = [w1 + "\t" + w2 for w1, w2 in zip(name, sex)]

    with open(args.file[2], "w") as f:
        f.write("\n".join(merge))


if __name__ == "__main__":
    main()
