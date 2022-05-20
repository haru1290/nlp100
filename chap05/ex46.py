from ex40 import get_option
from ex41 import get_chunk


def save_argument(sentences, path):
    with open(path, 'w') as f:
        for chunks in sentences:
            for chunk in chunks:
                for morph in chunk.morphs:
                    if morph.pos == '動詞':
                        cases = []
                        arguments = []
                        for src in chunk.srcs:
                            cases += [morph.surface for morph in chunks[src].morphs if morph.pos == '助詞'] 
                            arguments.append(''.join([morph.surface for morph in chunks[src].morphs]))

                        if len(cases) > 0:
                            cases = sorted(set(cases))
                            arguments = sorted(set(arguments), key=lambda x: x[-1:])
                            f.write(morph.base + '\t' + ' '.join(cases) + '\t' + ' '.join(arguments) + '\n')

                        break


def main():
    args = get_option()

    sentences = get_chunk(args.test)

    save_argument(sentences, args.result)


if __name__ == '__main__':
    main()
