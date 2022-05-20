from ex40 import get_option
from ex41 import get_chunk


def save_case(sentences, path):
    with open(path, 'w') as f:
        for chunks in sentences:
            for chunk in chunks:
                for morph in chunk.morphs:
                    if morph.pos == '動詞':
                        cases = []
                        for src in chunk.srcs:
                            cases += [morph.surface for morph in chunks[src].morphs if morph.pos == '助詞']

                        if len(cases) > 0:
                            v_cases = sorted(set(cases))
                            f.write(morph.base + '\t' + ' '.join(v_cases) + '\n')

                        break


def main():
    args = get_option()

    sentences = get_chunk(args.test)

    save_case(sentences, args.result)


if __name__ == '__main__':
    main()
