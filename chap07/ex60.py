from argparse import ArgumentParser
from gensim.models import KeyedVectors


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('--model', default='GoogleNews-vectors-negative300.bin')
    argparser.add_argument('--test1', default='questions-words.txt')
    argparser.add_argument('--test1_add', default='questions-words-add.txt')
    argparser.add_argument('--test2', default='combined.csv')
    argparser.add_argument('--result', default='result.png')

    return argparser.parse_args()


def main():
    args = get_option()

    model = KeyedVectors.load_word2vec_format(args.model, binary=True)

    print(model['United_States'])


if __name__ == '__main__':
    main()
