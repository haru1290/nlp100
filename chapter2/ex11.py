from ex10 import get_option
import re


def main():
    args = get_option()

    with open(args.file, "r") as f:
        print(re.sub("\t", " ", f.read()))


if __name__ == "__main__":
    main()
