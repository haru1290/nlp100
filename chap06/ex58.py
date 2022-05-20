from ex50 import get_option
from ex53 import predict
from sklearn.linear_model import LogisticRegression
from tqdm import tqdm
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def draw_graph(path, param):
    param = np.array(param).T

    fig = plt.figure()

    plt.plot(param[0], param[1], label='train')
    plt.plot(param[0], param[2], label='valid')
    plt.plot(param[0], param[3], label='test')
    plt.ylabel('Accuracy')
    plt.xlabel('C')
    plt.xscale ('log')
    plt.legend()

    fig.savefig(path)


def train(X_train, Y_train, C):
    lg = LogisticRegression(random_state=0, max_iter=10000, C=C)
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

    result = []
    for C in tqdm(np.logspace(-5, 4, 10, base=10)):
        lg = train(X_train, df_train['CATEGORY'], C)
    
        train_pred = predict(lg, X_train)
        valid_pred = predict(lg, X_valid)
        test_pred = predict(lg, X_test)

        train_accuracy = accuracy_score(df_train['CATEGORY'], train_pred[1])
        valid_accuracy = accuracy_score(df_valid['CATEGORY'], valid_pred[1])
        test_accuracy = accuracy_score(df_test['CATEGORY'], test_pred[1])

        result.append([C, train_accuracy, valid_accuracy, test_accuracy])

    draw_graph(args.result, result)


if __name__ == '__main__':
    main()
