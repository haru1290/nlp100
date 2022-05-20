from argparse import ArgumentParser


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('--corpus', default='neko.txt.mecab')
    argparser.add_argument('--result', default='result.png')
    return argparser.parse_args()


def get_morph(path):
    morphs = []
    sentences = []

    with open(path, 'r') as f:
        for morph in f:
            if morph != 'EOS\n':
                fields = morph.split()
                if len(fields) != 2:
                    continue
                attr = fields[1].split(',')
                morphs.append({'surface': fields[0], 'base': attr[6], 'pos': attr[0], 'pos1': attr[1]})
            else:
                sentences.append(morphs)
                morphs = []

    return sentences


def main():
    args = get_option()

    sentences = get_morph(args.corpus)

    for sentence in sentences[2]:
        print(sentence)


if __name__ == '__main__':
    main()
