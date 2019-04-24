import requests
import re

from requests.exceptions import RequestException

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/\
                    537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36\
                    QQBrowser/4.3.4986.400'
}


def get_one_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def main():
    url = 'http://maoyan.com/board/4?'
    html = get_one_page(url)
    print(html)


if __name__ == '__main__':
    main()