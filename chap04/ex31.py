from ex30 import get_option, get_morph


def get_verbs(sentences):
    verbs = []

    for sentence in sentences:
        for morph in sentence:
            if morph['pos'] == '動詞':
                verbs.append(morph['surface'])

    return verbs


def main():
    args = get_option()

    sentences = get_morph(args.corpus)

    verbs = set(get_verbs(sentences))

    print(f"動詞の表層系の数：{len(verbs)}\n")
    print("----------上位10件----------")
    print('\n'.join(list(verbs)[:10]))


if __name__ == '__main__':
    main()
