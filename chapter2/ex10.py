from argparse import ArgumentParser


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('--corpus', default='popular-names.txt')
    argparser.add_argument('--name', default='name.txt') 
    argparser.add_argument('--sex', default='sex.txt')
    argparser.add_argument('--merge', default='merge.txt')
    argparser.add_argument('--num', default=10)

    return argparser.parse_args()


def main():
    args = get_option()

    with open(args.corpus) as f:
        print(len(f.readlines()))


if __name__ == '__main__':
    main()
