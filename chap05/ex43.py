from ex40 import get_option
from ex41 import get_chunk


def show_dependency(sentences):
    chunks = sentences[2]
    for chunk in chunks:
        if chunk.dst != '-1':
            modifier = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])
            modifier_pos = [morph.pos for morph in chunk.morphs if morph.pos != '記号']
            modifiee = ''.join([morph.surface for morph in chunks[int(chunk.dst)].morphs if morph.pos != '記号'])
            modifiee_pos = [morph.pos for morph in chunks[int(chunk.dst)].morphs if morph.pos != '記号']

            if '名詞' in modifier_pos and '動詞' in modifiee_pos:
                print(modifier, modifiee ,sep='\t')


def main():
    args = get_option()

    sentences = get_chunk(args.corpus)

    show_dependency(sentences)


if __name__ == '__main__':
    main()
