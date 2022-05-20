from ex50 import get_option
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import string
import re


def preprocessing(text):
    table = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    text = text.translate(table)
    text = text.lower()
    text = re.sub(r'\d', '0', text)

    return text


def main():
    args = get_option()

    df_train = pd.read_csv(args.train, sep='\t')
    df_valid = pd.read_csv(args.valid, sep='\t')
    df_test = pd.read_csv(args.test, sep='\t')

    df =pd.concat([df_train, df_valid, df_test], axis=0, ignore_index=True)

    df['TITLE'] = df['TITLE'].map(lambda x: preprocessing(x))
 
    vectorizer = TfidfVectorizer(min_df=10, ngram_range=(1, 2))

    X_train_valid_test = vectorizer.fit_transform(df['TITLE'])
    X_train_valid_test = pd.DataFrame(X_train_valid_test.toarray(), columns=vectorizer.get_feature_names()) 

    X_train_valid = X_train_valid_test[:len(df_train) + len(df_valid)]
    X_train = X_train_valid[:len(df_train)]
    X_valid = X_train_valid[len(df_train):]
    X_test = X_train_valid_test[len(df_train) + len(df_valid):]
   
    X_train.to_csv(args.train_feature, sep='\t', index=False)
    X_valid.to_csv(args.valid_feature, sep='\t', index=False)
    X_test.to_csv(args.test_feature, sep='\t', index=False)


if __name__ == '__main__':
    main()
