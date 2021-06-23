from ex10 import get_option
from ex12 import get_col
from collections import Counter


def main():
    args = get_option()
        
    c = Counter(get_col(args.file, 0))

    name = [t[0] for t in c.most_common()]
    freq = [str(t[1]) for t in c.most_common()]

    print("\n".join([n + "\t" + f for n, f in zip(name, freq)]))


if __name__ == "__main__":
    main()
