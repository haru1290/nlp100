from ex60 import get_option
from gensim.models import KeyedVectors
import numpy as np
from matplotlib import pyplot as plt
import bhtsne


def main():
    args = get_option()

    model = KeyedVectors.load_word2vec_format(args.model, binary=True)

    countries = set()
    with open(args.test1_add, 'r') as f:
        for r in f:
            r = r.split()
            if r[0] in ['capital-common-countries', 'capital-world']:
                countries.add(r[2])
            elif r[0] in ['currency', 'gram6-nationality-adjective']:
                countries.add(r[1])

    countries = list(countries)
    countries_vec = [model[country] for country in countries]

    embedded = bhtsne.tsne(np.array(countries_vec).astype(np.float64), dimensions=2)

    fig = plt.figure(figsize=(10, 10))
    plt.scatter(np.array(embedded).T[0], np.array(embedded).T[1])
    for (x, y), name in zip(embedded, countries):
        plt.annotate(name, (x, y))
    fig.savefig(args.result)


if __name__ == '__main__':
    main()
