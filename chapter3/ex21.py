from ex20 import get_option, get_uk_text
import re


def get_category_row(text):
    regex = r'^(\[\[Category:.*\]\])$'
    text = '\n'.join(re.findall(regex, text, re.MULTILINE))

    return text


def main():
    args = get_option()
    
    uk_text = get_uk_text(args.corpus)    
    result = get_category_row(uk_text)

    print(result)


if __name__ == '__main__':
    main()
