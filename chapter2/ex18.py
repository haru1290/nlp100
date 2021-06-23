def sort_rows(path):
    with open(path, "r") as f:
        rows = [r.split() for r in f.readlines()]
        s_rows = "\n".join(["\t".join(r) for r in sorted(rows, key=lambda x: int(x[2]), reverse=True)])

    return s_rows


def main():
    path = "./popular-names.txt"
    
    print(sort_rows(path))


if __name__ == "__main__":
    main()
