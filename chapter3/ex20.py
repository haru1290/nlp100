from argparse import ArgumentParser
import json


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('--corpus', default='jawiki-country.json')

    return argparser.parse_args()


def get_uk_text(path):
    with open(path, 'r') as f:
        for r in f:
            jsn = json.loads(r)
            if jsn['title'] == 'イギリス':
                uk_text = jsn['text']
                break

    return uk_text


def main():
    args = get_option()

    result = get_uk_text(args.corpus)

    print(result)


if __name__ == '__main__':
    main()
