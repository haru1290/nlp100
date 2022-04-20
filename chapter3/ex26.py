from ex20 import get_option, get_uk_text
from ex25 import get_template
import re


def remove_emphasis(text):
    regex = r'\'{2,5}'
    text = re.sub(regex, '', text)

    return text


def main():
    args = get_option()

    uk_text = get_uk_text(args.corpus)
    template = get_template(uk_text)
    result = {k : remove_emphasis(v) for k, v in template.items()}

    for k, v in result.items():
        print(k + ' : ' + v)


if __name__ == '__main__':
    main()
