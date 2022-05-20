from ex20 import get_option, get_uk_text
import re


def get_file(text):
    regex = r'\[\[ファイル:(.+?)\|'
    text = '\n'.join(re.findall(regex, text))

    return text


def main():
    args = get_option()
    
    uk_text = get_uk_text(args.corpus)
    result = get_file(uk_text)

    print(result)


if __name__ == '__main__':
    main()
