from ex40 import get_option
from ex41 import get_chunk
from graphviz import Digraph


def save_dependency(sentences):
    dg = Digraph(format='png')

    chunks = sentences[2]
    for chunk in chunks:
        if chunk.dst != '-1':
            modifier = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])
            modifiee = ''.join([morph.surface for morph in chunks[int(chunk.dst)].morphs if morph.pos != '記号'])

            dg.edge(modifier, modifiee)

    dg.render()


def main():
    args = get_option()

    sentences = get_chunk(args.corpus)

    save_dependency(sentences)


if __name__ == '__main__':
    main()
