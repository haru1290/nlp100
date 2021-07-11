from ex20 import get_option, get_uk_text
import re


def get_section(text):
    regex = r'^(\={2,})\s*(.+?)\s*(\={2,})$'
    text = '\n'.join([r[1] + ':' + str(len(r[0]) - 1) for r in re.findall(regex, text, re.MULTILINE)])

    return text


def main():
    args = get_option()
    
    uk_text = get_uk_text(args.corpus)
    result = get_section(uk_text) 

    print(result)


if __name__ == '__main__':
    main()
