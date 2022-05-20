from ex50 import get_option
from ex52 import train
from ex53 import predict
from sklearn.metrics import precision_score, recall_score, f1_score
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

    test_precision = precision_score(df_test['CATEGORY'], test_pred[1], average=None, labels=['b', 'e', 't', 'm'])
    test_precision = np.append(test_precision, precision_score(df_test['CATEGORY'], test_pred[1], average='micro'))
    test_precision = np.append(test_precision, precision_score(df_test['CATEGORY'], test_pred[1], average='macro'))
    
    test_recall = recall_score(df_test['CATEGORY'], test_pred[1], average=None, labels=['b', 'e', 't', 'm'])
    test_recall = np.append(test_recall, recall_score(df_test['CATEGORY'], test_pred[1], average='micro'))
    test_recall = np.append(test_recall, recall_score(df_test['CATEGORY'], test_pred[1], average='macro'))
    
    test_f1 = f1_score(df_test['CATEGORY'], test_pred[1], average=None, labels=['b', 'e', 't', 'm'])
    test_f1 = np.append(test_f1, f1_score(df_test['CATEGORY'], test_pred[1], average='micro'))
    test_f1 = np.append(test_f1, f1_score(df_test['CATEGORY'], test_pred[1], average='macro'))

    scores = pd.DataFrame({'適合率': test_precision, '再現率': test_recall, 'F1': test_f1}, index=['b', 'e', 't', 'm', 'マイクロ平均', 'マクロ平均'])

    print(scores)


if __name__ == '__main__':
    main()
