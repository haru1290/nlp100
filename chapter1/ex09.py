import random


def typoglycemia(s):
    splits = s.split()
    lst = []

    for w in splits:
        if len(w) >= 4:
            lst.append(w[:1] + "".join(random.sample(w[1:-1], len(w[1:-1]))) + w[-1:])
        else:
            lst.append(w)
    
    return " ".join(lst)


def main():
    s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    print(typoglycemia(s))


if __name__ == "__main__":
    main()
