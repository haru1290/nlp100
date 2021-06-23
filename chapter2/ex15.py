from ex14 import get_option


def tail(path, n):
    with open(path, "r") as f:
        rows = f.readlines()

    return "".join(rows[-int(n):])


def main():
    args = get_option()

    print(tail(args.file, args.num))


if __name__ == "__main__":
    main()

