from ex12 import get_col


def main():
    path1 = "./col1.txt"
    path2 = "./col2.txt"
    path3 = "./col12.txt"

    name = get_col(path1, 0)
    sex = get_col(path2, 0)

    merge = [w1 + "\t" + w2 for w1, w2 in zip(name, sex)]

    with open(path3, "w") as f:
        f.write("\n".join(merge))


if __name__ == "__main__":
    main()
