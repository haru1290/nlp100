import sys


def split_file(n):
    path = "./popular-names.txt"
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
    for rows in split_file(sys.argv[1]):
        print("".join(rows))
        print("size : {}".format(len(rows)))
        print("----------------------------------------")


if __name__ == "__main__":
    main()

