from argparse import ArgumentParser


class Morph:
    def __init__(self, morph):
        surface, attr = morph.split()
        attr = attr.split(',')
        self.surface = surface
        self.base = attr[6]
        self.pos = attr[0]
        self.pos1 = attr[1]


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('--corpus', default='ai.ja.txt.parsed')
    argparser.add_argument('--test', default='test.txt.parsed')
    argparser.add_argument('--result', default='result.txt')

    return argparser.parse_args()


def get_morph(path):
    morphs = []
    sentences = []

    with open(path, 'r') as f:
        for morph in f:
            if morph[0] == '*':
                continue
            elif morph != 'EOS\n':
                morphs.append(Morph(morph))
            else:
                sentences.append(morphs)
                morphs = []

    return sentences


def main():
    args = get_option()

    sentences = get_morph(args.corpus)

    for sentence in sentences[2]:
        print(vars(sentence))


if __name__ == '__main__':
    main()
