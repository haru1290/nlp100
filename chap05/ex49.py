from ex40 import get_option
from ex41 import get_chunk
from itertools import combinations
import re


def show_nouns_path(sentences):
    nouns = []
    for chunks in sentences:
        for i, chunk in enumerate(chunks):
            if '名詞' in [morph.pos for morph in chunk.morphs]:
                nouns.append(i)
        for i, j in combinations(nouns, 2):
            path_i = []
            path_j = []
            while i != j:
                if i < j:
                    path_i.append(i)
                    i = int(chunks[i].dst)
                else:
                    path_j.append(j)
                    j = int(chunks[j].dst)
            if len(path_i) != 0:
                if len(path_j) == 0:
                    chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in chunks[path_i[0]].morphs])
                    chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in chunks[i].morphs])
                    chunk_X = re.sub('X+', 'X', chunk_X)
                    chunk_Y = re.sub('Y+', 'Y', chunk_Y)
                    path_XtoY = [chunk_X] + [''.join([morph.surface for morph in chunks[n].morphs]) for n in path_i[1:]] + [chunk_Y]

                    print(' -> '.join(path_XtoY))
                else:
                    chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in chunks[path_i[0]].morphs])
                    chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in chunks[path_j[0]].morphs])
                    chunk_K = ''.join([morph.surface for morph in chunks[i].morphs])
                    chunk_X = re.sub('X+', 'X', chunk_X)
                    chunk_Y = re.sub('Y+', 'Y', chunk_Y)
                    path_X = [chunk_X] + [''.join([morph.surface for morph in chunks[n].morphs]) for n in path_i[1:]]
                    path_Y = [chunk_Y] + [''.join([morph.surface for morph in chunks[n].morphs]) for n in path_j[1:]]

                    print(' | '.join([' -> '.join(path_X), ' -> '.join(path_Y), chunk_K]))


def main():
    args = get_option()

    sentences = get_chunk(args.corpus)

    show_nouns_path(sentences)


if __name__ == '__main__':
    main()
