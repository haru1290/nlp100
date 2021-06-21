def n_gram(n, lst):
    return list(zip(*[lst[i:] for i in range(n)]))

def main():
    s = "I am an NLPer"
    splits = s.split()

    print("単語bi-gram", n_gram(2,splits))
    print("文字bi-gram", n_gram(2,s))

if __name__ == "__main__":
    main()
