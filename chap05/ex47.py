from ex40 import get_option
from ex41 import get_chunk


def save_predicate(sentences, path):
    with open(path, 'w') as f:
        for chunks in sentences:
            for chunk in chunks:
                for morph in chunk.morphs:
                    if morph.pos == '動詞':
                        for i, src in enumerate(chunk.srcs):
                            if len(chunks[src].morphs) == 2 and chunks[src].morphs[0].pos1 == 'サ変接続' and chunks[src].morphs[1].surface == 'を':
                                predicate = chunks[src].morphs[0].surface + chunks[src].morphs[1].surface + morph.base
                                cases = []
                                arguments = []
                                for src_r in chunk.srcs[:i] + chunk.srcs[i + 1:]:
                                    cases += [morph.surface for morph in chunks[src_r].morphs if morph.pos == '助詞']
                                    arguments.append(''.join([morph.surface for morph in chunks[src_r].morphs]))

                                if len(cases) > 0 and predicate != '':
                                    cases = sorted(set(cases))
                                    arguments = sorted(set(arguments), key=lambda x: x[-1:])
                                    f.write(predicate + '\t' + ' '.join(cases) + '\t' + ' '.join(arguments) + '\n')
                        
                        break



def main():
    args = get_option()

    sentences = get_chunk(args.test)

    save_predicate(sentences, args.result)


if __name__ == '__main__':
    main()
