from ex60 import get_option
from gensim.models import KeyedVectors


def main():
    args = get_option()

    model = KeyedVectors.load_word2vec_format(args.model, binary=True)

    with open(args.test1, 'r') as f1, open(args.test1_add, 'w') as f2:
        for r in f1:
            r = r.split()
            if r[0] == ':':
                category = r[1]
            else:
                word, cos = model.most_similar(positive=[r[1], r[2]], negative=[r[0]], topn=1)[0]
                r.extend([word, str(cos)])
                f2.write(category + ' ' + ' '.join(r) + '\n')


if __name__ == '__main__':
    main()
