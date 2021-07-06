from ex10  import get_option


def sort_rows(path):
    with open(path) as f:
        rows = [r.split() for r in f.readlines()]
        s_rows = '\n'.join(['\t'.join(r) for r in sorted(rows, key=lambda x: int(x[2]), reverse=True)])

    return s_rows


def main():
    args = get_option()
    
    print(sort_rows(args.corpus))


if __name__ == "__main__":
    main()
