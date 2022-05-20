from ex60 import get_option
from gensim.models import KeyedVectors
import numpy as np
from sklearn.cluster import KMeans


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
    
    cls = KMeans(n_clusters=5)
    cls.fit(countries_vec)
    
    for i in range(5):
        cluster = np.where(cls.labels_ == i)[0]
        print('cluster:', i)
        print(', '.join([countries[k] for k in cluster]))


if __name__ == '__main__':
    main()
