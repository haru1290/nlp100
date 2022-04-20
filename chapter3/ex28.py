from ex20 import get_option, get_uk_text
from ex25 import get_template
from ex26 import remove_emphasis
from ex27 import remove_links
import re


def remove_markup(text):
    #ファイルの除去
    regex = r'\[\[ファイル:.+?\]\]'
    text = re.sub(regex, '', text)
    
    #外部リンクの除去
    regex = r'\[https?:\/\/.*\]|https?:\/\/.*\|'
    text = re.sub(regex, '', text)

    #htmlタグの除去
    regex = r'<.+?>'
    text = re.sub(regex, '', text)

    #テンプレート除去
    regex = r'\{\{.+?\}\}'
    text = re.sub(regex, '', text)
    
    return text


def main():
    args = get_option()

    uk_text = get_uk_text(args.corpus)
    template = get_template(uk_text)
    template = {k : remove_emphasis(v) for k, v in template.items()}
    template = {k : remove_links(v) for k, v in template.items()}
    result = {k : remove_markup(v) for k, v in template.items()}

    for k, v in result.items():
        print(k + ' : ' + v)


if __name__ == '__main__':
    main()
