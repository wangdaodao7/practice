import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError
import json

MONGO_URL = 'localhost'
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'
GROUP_START = 1
GROUP_END = 20
KEWWORD = '街拍'


def get_page_index(offset, keyword):
    data = {
        'autoload':'true',
        'count':'20',
        'format':'json',
        'keyword':keyword,
        'offset': offset
    }
    params = urlencode(data)
    base =  'http://www.toutiao.com/search_content/'
    url = base + '?' + params
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('请求页面错误')
        return None

def parse_page_index(text):
    try:
        data = json.loads(text)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                
                yield item.get('article_url')
    except ConnectionError:
        print('出现错误。')
        return None
    





