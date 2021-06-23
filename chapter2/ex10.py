from argparse import ArgumentParser


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('-f', '--file', default='popular-names.txt')

    return argparser.parse_args()


def main():
    args = get_option()

    with open(args.file, "r") as f:
        print(len(f.readlines()))


if __name__ == "__main__":
    main()
