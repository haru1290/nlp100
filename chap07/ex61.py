from ex60 import get_option
from gensim.models import KeyedVectors


def main():
    args = get_option()

    model = KeyedVectors.load_word2vec_format(args.model, binary=True)

    print(model.similarity('United_States', 'U.S.'))


if __name__ == '__main__':
    main()
