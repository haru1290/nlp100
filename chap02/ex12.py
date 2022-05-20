from ex10 import get_option


def get_col(path, num):
    with open(path) as f:
        rows = [r.split() for r in f.readlines()]
        col = [r[num] for r in rows]

    return col


def main():
    args = get_option()

    name = get_col(args.corpus, 0)
    sex = get_col(args.corpus, 1)

    with open(args.name, 'w') as f:
        f.write('\n'.join(name))

    with open(args.sex, 'w') as f:
        f.write('\n'.join(sex))


if __name__ == '__main__':
    main()
