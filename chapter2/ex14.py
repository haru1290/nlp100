from argparse import ArgumentParser


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('-f', '--file', default='popular-names.txt')
    argparser.add_argument('-n', '--num', default=10, type=int)

    return argparser.parse_args()


def head(path, n):
    with open(path, "r") as f:
        rows = f.readlines()

    return "".join(rows[:int(n)])


def main():
    args = get_option()

    print(head(args.file, args.num))


if __name__ == "__main__":
    main()

