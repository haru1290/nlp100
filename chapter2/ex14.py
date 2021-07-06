from ex10 import get_option


def head(path, n):
    with open(path) as f:
        rows = f.readlines()

    return ''.join(rows[:int(n)])


def main():
    args = get_option()

    print(head(args.corpus, args.num))


if __name__ == '__main__':
    main()

