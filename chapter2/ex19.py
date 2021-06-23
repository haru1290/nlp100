from collections import Counter
from ex12 import get_col


def main():
    path = "./popular-names.txt"
        
    c = Counter(get_col(path, 0))

    name = [t[0] for t in c.most_common()]
    freq = [str(t[1]) for t in c.most_common()]

    print("\n".join([n + "\t" + f for n, f in zip(name, freq)]))


if __name__ == "__main__":
    main()
