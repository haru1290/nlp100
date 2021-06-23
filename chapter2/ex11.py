import re


def main():
    path = "./popular-names.txt"

    with open(path, "r") as f:
        print(re.sub("\t", " ", f.read()))


if __name__ == "__main__":
    main()
