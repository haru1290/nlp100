from ex40 import Morph, get_option


class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []


def get_chunk(path):
    morphs = []
    chunks = []
    sentences = []

    with open(path, 'r') as f:
        for row in f:
            if row[0] == '*':
                if len(morphs) != 0:
                    chunks.append(Chunk(morphs, dst))
                    morphs = []
                dst = row.split()[2].rstrip('D')
            elif row != 'EOS\n':
                morphs.append(Morph(row))
            else:
                chunks.append(Chunk(morphs, dst))
                sentences.append(chunks)
                morphs = []
                chunks = []

    for chunks in sentences:
        for i, chunk in enumerate(chunks):
            if chunk.dst != '-1':
                chunks[int(chunk.dst)].srcs.append(i)

    return sentences


def main():
    args = get_option()

    sentences = get_chunk(args.corpus)

    for chunk in sentences[2]:
        print([morph.surface for morph in chunk.morphs], chunk.dst, chunk.srcs)


if __name__ == '__main__':
    main()
