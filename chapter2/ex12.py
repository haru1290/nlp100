def get_col(path, num):
    with open(path, "r") as f:
        rows = [r.split() for r in f.readlines()]
        col = [r[num] for r in rows]

    return col


def main():
    path = "./popular-names.txt"

    col1 = get_col(path, 0)
    col2 = get_col(path, 1)

    with open("./col1.txt", "w") as f:
        f.write("\n".join(col1))

    with open("./col2.txt", "w") as f:
        f.write("\n".join(col2))


if __name__ == "__main__":
    main()
