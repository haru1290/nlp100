from argparse import ArgumentParser
from sklearn.model_selection import train_test_split
import pandas as pd


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('--corpus', default='newsCorpora.csv')
    
    argparser.add_argument('--train', default='train.txt')
    argparser.add_argument('--valid', default='valid.txt')
    argparser.add_argument('--test', default='test.txt')
    
    argparser.add_argument('--train_feature', default='train.feature.txt')
    argparser.add_argument('--valid_feature', default='valid.feature.txt')
    argparser.add_argument('--test_feature', default='test.feature.txt')
    
    argparser.add_argument('--result', default='result.png')

    return argparser.parse_args()


def main():
    args = get_option()
    
    df = pd.read_csv(args.corpus, header=None, sep='\t', names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])

    df = df.query('PUBLISHER in ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]')

    df_train, df_valid_test = train_test_split(df, train_size=0.8, shuffle=True, random_state=0, stratify=df['CATEGORY'])
    df_valid, df_test = train_test_split(df_valid_test, train_size=0.5, shuffle=True, random_state=0, stratify=df_valid_test['CATEGORY'])

    df_train.to_csv(args.train, sep='\t', index=False)
    df_valid.to_csv(args.valid, sep='\t', index=False)
    df_test.to_csv(args.test, sep='\t', index=False)

    print('学習データ')
    print(df_train['CATEGORY'].value_counts())
    print('検証データ')
    print(df_valid['CATEGORY'].value_counts())
    print('評価データ')
    print(df_test['CATEGORY'].value_counts())


if __name__ == '__main__':
    main()

