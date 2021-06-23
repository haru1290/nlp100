from ex12 import get_col


def main():
    path = "./popular-names.txt"

    col = get_col(path, 0)

    print(set(col))


if __name__ == "__main__":
    main()
