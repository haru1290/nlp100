from ex20 import get_option, get_uk_text
from ex25 import get_template
import re
import requests


def get_url(template):
    img = re.sub(' ', '_', template['国旗画像'])

    S = requests.Session()

    URL = 'https://en.wikipedia.org/w/api.php'
    PARAMS = {
        'action': 'query',
        'format': 'json',
        'prop': 'imageinfo',
        'iiprop': 'url',
        'titles': 'File:' + img
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    IMAGEINFO = DATA['query']['pages']['23473560']['imageinfo']

    return IMAGEINFO


def main():
    args = get_option()
    
    uk_text = get_uk_text(args.corpus)
    template = get_template(uk_text)
    result = get_url(template)

    print(result[0]['url'])


if __name__ == '__main__':
    main()
