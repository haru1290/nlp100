from ex10 import get_option
from ex12 import get_col


def main():
    args = get_option()

    name = get_col(args.file, 0)

    print(set(name))


if __name__ == "__main__":
    main()
