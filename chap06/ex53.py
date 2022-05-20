from ex50 import get_option
from ex52 import train
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np


def predict(lg, X):
    return ([np.max(lg.predict_proba(X), axis=1), lg.predict(X)])


def main():
    args = get_option()

    df_train = pd.read_csv(args.train, sep='\t')
    df_valid = pd.read_csv(args.valid, sep='\t')
    df_test = pd.read_csv(args.test, sep='\t')

    X_train = pd.read_csv(args.train_feature, sep='\t')
    X_valid = pd.read_csv(args.valid_feature, sep='\t')
    X_test = pd.read_csv(args.test_feature, sep='\t')

    lg = train(X_train, df_train['CATEGORY'])
 
    train_pred = predict(lg, X_train)
    test_pred = predict(lg, X_test)


if __name__ == '__main__':
    main()
