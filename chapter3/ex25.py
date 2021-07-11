from ex20 import get_option, get_uk_text
import re


def get_template(text):
    regex = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    template = re.findall(regex, text, re.MULTILINE + re.DOTALL)

    regex = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    template = dict(re.findall(regex, template[0], re.MULTILINE + re.DOTALL))
    
    return template


def main():
    args = get_option()

    uk_text = get_uk_text(args.corpus)
    result = get_template(uk_text)

    for k, v in result.items():
        print(k + ' : ' + v)


if __name__ == '__main__':
    main()
