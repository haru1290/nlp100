from ex05 import n_gram

def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"
    X = set(n_gram(2, s1))
    Y = set(n_gram(2, s2))

    print("X=", X)
    print("Y=", Y)
    print("和集合", X | Y)
    print("積集合", X & Y)
    print("差集合", X - Y)
    print("Xにseが含まれるか？", {('s', 'e')} <= X)
    print("Yにseが含まれるか？", {('s', 'e')} <= Y)

if __name__ == "__main__":
    main()
