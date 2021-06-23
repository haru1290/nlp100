from ex14 import get_option


def split_file(path, n):
    lst = []
    i = 0

    with open(path, "r") as f:
        rows = f.readlines()
        row_num = len(rows)
        step = round(row_num / int(n))

        while i < row_num:
            lst.append(rows[i:i+step])
            i += step        

    return lst


def main():
    args = get_option()

    for rows in split_file(args.file, args.num):
        print("".join(rows))
        print("size : {}".format(len(rows)))
        print("----------------------------------------")


if __name__ == "__main__":
    main()

