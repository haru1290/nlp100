import re


def main():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    splits = re.sub("[,|.]", "", s).split()
    ans = [len(i) for i in splits]

    print(ans)


if __name__ == "__main__":
    main()
