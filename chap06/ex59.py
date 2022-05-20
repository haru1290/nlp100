from ex50 import get_option
from ex53 import predict
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import optuna


class Objective:
    def __init__(self, X_train, Y_train, X_valid, Y_valid):
        self.X_train = X_train
        self.Y_train = Y_train
        self.X_valid = X_valid
        self.Y_valid = Y_valid

    def __call__(self, trial):
        l1_ratio = trial.suggest_uniform('l1_ratio', 0, 1)
        C = trial.suggest_loguniform('C', 1e-4, 1e4)
        
        lg = LogisticRegression(random_state=0, max_iter=10000, solver='saga', l1_ratio=l1_ratio, C=C)
        lg.fit(self.X_train, self.Y_train)

        valid_pred = predict(lg, self.X_valid)

        valid_accuracy = accuracy_score(self.Y_valid, valid_pred[1])

        return valid_accuracy 


def train(trial, X_train, Y_train):
    l1_ratio = trial.params['l1_ratio']
    C = trial.params['C']

    lg = LogisticRegression(random_state=0, max_iter=10000, penalty='elasticnet', solver='saga', l1_ratio=l1_ratio, C=C)
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

    objective = Objective(X_train, df_train['CATEGORY'], X_valid, df_valid['CATEGORY'])
   
    study = optuna.create_study(direction='maximize')
    study.optimize(objective, timeout=3600)
    
    lg = train(study.best_trial, X_train, df_train['CATEGORY'])

    train_pred = predict(lg, X_train)
    valid_pred = predict(lg, X_valid)
    test_pred = predict(lg, X_test)

    train_accuracy = accuracy_score(df_train['CATEGORY'], train_pred[1])
    valid_accuracy = accuracy_score(df_valid['CATEGORY'], valid_pred[1])
    test_accuracy = accuracy_score(df_test['CATEGORY'], test_pred[1])

    print('Best trial:', study.best_trial)

    print("学習データの正解率：{}".format(train_accuracy))
    print("検証データの正解率：{}".format(valid_accuracy))
    print("評価データの正解率：{}".format(test_accuracy))

    
if __name__ == '__main__':
    main()
