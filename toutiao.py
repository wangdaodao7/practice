import json
import os
import re
from hashlib import md5
from json.decoder import JSONDecodeError
from multiprocessing import Pool
from urllib.parse import urlencode

import pymongo
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

MONGO_URL = 'localhost'
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'
GROUP_START = 1
GROUP_END = 3
KEWWORD = '街拍'

client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 QQBrowser/4.3.4986.400'
}
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

def save_image(content):
    file_path = '{0}/img/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        print('正在下载图片')
        print(file_path)
        with open(file_path, 'wb') as f:
            f.write(content)
    else:
        print('已存在')


def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except ConnectionError:
        return None


def get_page_detail(url):
    try:
        response = requests.get(url, headers=headers)
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
        sub_imagers = data.get('sub_images')
        images = [item.get('url') for item in sub_imagers]
        for image in images:
            download_image(image)
        return {
                'title': title,
                'url': url,
                'images': images}
        

def save_to_mango(reslut):
    if db[MONGO_TABLE].insert(reslut):
        print('储存数据库成功')
        return True
    return False


def main(offset):
    text = get_page_index(offset, KEWWORD)
    urls = parse_page_index(text)
    for url in urls:
        if url and 'group' in url:
            html = get_page_detail(url) 
            reslut = parse_page_detail(html, url)
            if reslut:
                save_to_mango(reslut)

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
    print(groups)
    pool.map(main, groups)
    pool.close()
    pool.join()
