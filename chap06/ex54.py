from ex50 import get_option
from ex52 import train
from ex53 import predict
from sklearn.metrics import accuracy_score
import pandas as pd


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

    train_accuracy = accuracy_score(df_train['CATEGORY'], train_pred[1])
    test_accuracy = accuracy_score(df_test['CATEGORY'], test_pred[1])

    print("学習データの正解率：{}".format(train_accuracy))
    print("評価データの正解率：{}".format(test_accuracy))
    

if __name__ == '__main__':
    main()
