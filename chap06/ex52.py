from ex50 import get_option
from sklearn.linear_model import LogisticRegression
import pandas as pd


def train(X_train, Y_train):
    lg = LogisticRegression(random_state=0, max_iter=10000)
    lg.fit(X_train, Y_train)

    return lg


def main():
    args = get_option()

    df_train = pd.read_csv(args.train, sep='\t')
    df_valid = pd.read_csv(args.valid, sep='\t')
    df_test = pd.read_csv(args.test, sep='\t')
    
    X_train = pd.read_csv(args.train_feature, sep='\t')
    X_valid = pd.read_csv(args.valid_feature, sep='\t')
    X_test = pd.read_csv(args.test_feature, sep='\t')

    print(train(X_train, df_train['CATEGORY']))


if __name__ == '__main__':
    main()
