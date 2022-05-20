from ex60 import get_option
from gensim.models import KeyedVectors
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


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

    fig = plt.figure(figsize=(15, 5))    
    Z = linkage(countries_vec, method='ward')
    dendrogram(Z, labels=countries)
    fig.savefig(args.result)


if __name__ == '__main__':
    main()
