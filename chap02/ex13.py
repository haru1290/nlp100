from ex10 import get_option
from ex12 import get_col


def main():
    args = get_option()

    name = get_col(args.name, 0)
    sex = get_col(args.sex, 0)

    merge = [w1 + '\t' + w2 for w1, w2 in zip(name, sex)]

    with open(args.merge, 'w') as f:
        f.write('\n'.join(merge))


if __name__ == '__main__':
    main()
