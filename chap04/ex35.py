from ex30 import get_option, get_morph
import collections

def get_freq(sentences):
    freq = []

    for sentence in sentences:
        for morph in sentence:
            freq.append(morph['surface'])

    c = collections.Counter(freq)
    
    return c.most_common()


def main():
    args = get_option()

    sentences = get_morph(args.corpus)

    freq = get_freq(sentences)

    print("----------上位10件----------")
    for f in freq[:10]:
        print(f)


if __name__ == '__main__':
    main()
