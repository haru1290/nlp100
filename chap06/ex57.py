from ex50 import get_option
from ex52 import train
from ex53 import predict
import pandas as pd
import numpy as np


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

    features = X_train.columns.values
    i = list(range(1, 11))
    for category, coef in zip(lg.classes_, lg.coef_):
        print('CATEGORY：{}'.format(category))
        best_features = pd.DataFrame(features[np.argsort(coef)[::-1][:10]], columns=['上位10'], index=i).T
        worst_features = pd.DataFrame(features[np.argsort(coef)[:10]], columns=['下位10'], index=i).T
        print(pd.concat([best_features, worst_features], axis=0))
        print('\t')

    
if __name__ == '__main__':
    main()
