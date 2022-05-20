from ex30 import get_option, get_morph
from ex36 import plot_graph
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import japanize_matplotlib
import collections


def get_freq(sentences):
    freq = []

    for sentence in sentences:
        for i in range(1, len(sentence)-2):
            if sentence[i]['surface'] == '猫':
                freq.append(sentence[i-1]['surface'])
                freq.append(sentence[i+1]['surface'])

    c = collections.Counter(freq)

    return c.most_common(10)


def main():
    args = get_option()

    sentences = get_morph(args.corpus)

    freq = get_freq(sentences)

    plot_graph(args.result, freq)


if __name__ == '__main__':
    main()
