import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError
import json
from bs4 import BeautifulSoup


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

def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('发生错误')
        return None

def parse_page_detail(text, url):
    soup = BeautifulSoup(text, 'lxml')
    reslut = soup.select('title')
    title = reslut[0].get_text() if reslut else ''
    images_pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)
    reslut = re.search(images_pattern, text)
    if reslut:
        data = json.loads(reslut.group(1).replace('\\', ''))
        










def download_image(url):
    # print('正在下载图片')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('正在下载图片')
            # save_image(response.content)
        return None
    except ConnectionError:
        return None


html = get_page_index(10, KEWWORD)

for x in parse_page_index(html):
    print(x)
    if x: 
        download_image(x)



    