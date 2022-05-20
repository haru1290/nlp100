from ex30 import get_option, get_morph


def get_nouns(sentences):
    nouns = []
    nouns_lst = []
    cnt = 0

    for sentence in sentences:
        for morph in sentence:
            if morph['pos'] == '名詞':
                nouns.append(morph['surface'])
                cnt += 1
            else:
                if cnt >= 2:
                    nouns_lst.append(''.join(nouns))
                nouns = []
                cnt = 0

    return nouns_lst


def main():
    args = get_option()

    sentences = get_morph(args.corpus)

    nouns = set(get_nouns(sentences))

    print(f"名詞の連接の数：{len(nouns)}\n")
    print("----------上位10件----------")
    print('\n'.join(list(nouns)[:10]))


if __name__ == '__main__':
    main()
