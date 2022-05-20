from ex60 import get_option
from gensim.models import KeyedVectors
import numpy as np
from scipy.stats import spearmanr
import re


def main():
    args = get_option()

    model = KeyedVectors.load_word2vec_format(args.model, binary=True)

    ws353 = []
    with open(args.test2, 'r') as f:
        next(f)
        for r in f:
            r = re.sub('\n', '', r)
            r = r.split(',')
            r.append(model.similarity(r[0], r[1]))
            ws353.append(r)

    human = np.array(ws353).T[2]
    cos = np.array(ws353).T[3]
    correlation, pvalue = spearmanr(human, cos)

    print(f"スピアマン相関係数：{correlation:.3f}")


if __name__ == '__main__':
    main()
