from ex40 import get_option
from ex41 import get_chunk


def show_noun_path(sentences):
    for chunks in sentences:
        for chunk in chunks:
            if '名詞' in [morph.pos for morph in chunk.morphs]:
                path = [''.join([morph.surface for morph in chunk.morphs])]
                while chunk.dst != '-1':
                    path.append(''.join([morph.surface for morph in chunks[int(chunk.dst)].morphs]))
                    chunk = chunks[int(chunk.dst)]

                print(' -> '.join(path))


def main():
    args = get_option()

    sentences = get_chunk(args.test)

    show_noun_path(sentences)


if __name__ == '__main__':
    main()
