def main():
    path = "./popular-names.txt"

    with open(path, "r") as f:
        print(len(f.readlines()))


if __name__ == "__main__":
    main()
