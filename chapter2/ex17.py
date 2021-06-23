from ex12 import get_col


def main():
    path = "./popular-names.txt"

    name = get_col(path, 0)

    print(set(name))


if __name__ == "__main__":
    main()
