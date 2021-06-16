def n_gram(n, lst):
    return list(zip(*[lst[i:] for i in range(n)]))

str = "I am an NLPer"
splits = str.split()
print("単語bi-gram", n_gram(2,splits))
print("文字bi-gram", n_gram(2,str))
