from ex30 import get_option, get_morph


def get_nouns(sentences):
    nouns = []
    
    for sentence in sentences:
        for i in range(1, len(sentence)-2):
            if sentence[i-1]['pos'] == '名詞' and sentence[i]['surface'] == 'の' and sentence[i+1]['pos'] == '名詞':
                nouns.append(sentence[i-1]['surface'] + sentence[i]['surface'] + sentence[i+1]['surface'])

    return nouns


def main():
    args = get_option()

    sentences = get_morph(args.corpus)

    nouns = set(get_nouns(sentences))

    print(f"'の'で連結された名詞句の数：{len(nouns)}\n")
    print("----------上位10件----------")
    print('\n'.join(list(nouns)[:10]))


if __name__ == '__main__':
    main()
