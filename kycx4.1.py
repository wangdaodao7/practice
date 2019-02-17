
import requests
from bs4 import BeautifulSoup
import lxml
import datetime
import time
import itchat

url = 'https://yz.chsi.com.cn/apply/cjcx/cjcx.do'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Content-Length': '94',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'yz.chsi.com.cn',
    'Origin': 'https://yz.chsi.com.cn',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://yz.chsi.com.cn/apply/cjcx/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400  ',
}

data = {
    'xm': '孙一文',
    'zjhm': '370304199707191020',
    'ksbh': '100279218380529',
    'bkdwdm': '',
    'checkcode': ''
}


def get_info():
    response = requests.post(url, data=data, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        if soup.select('.zx-no-answer'):
            txt = soup.select('.zx-no-answer')[0].text
            msg = '---结果未出---\n{}'.format(txt)
        elif soup.select('.yzwb-alert-msg'):
            txt = soup.select('.zx-no-answer')[0].text
            msg = '---结果未出---\n{}'.format(txt)
        else:
            msg = '我考上了！'
        return msg


def send_info():
    now_hour = datetime.datetime.now().hour
    now_minute = datetime.datetime.now().minute
    now_second = datetime.datetime.now().second
    now_time = '{}:{}:{}'.format(now_hour, now_minute, now_second)

    if now_second == 0:
        reslut = '{1}:\n{0}'.format(get_info(), now_time)
        print(reslut)
        if now_minute == 0:
            itchat.send(reslut, username=username)
        if '考上' in reslut:
            itchat.send('可能考研结果出来了，等确认中', toUserName=username)
            itchat.send('可能考研结果出来了，等确认中', toUserName=username)

    else:
        print(now_time)


itchat.auto_login(hotReload=True)
users = itchat.search_friends('孙妞')
print('登陆成功！！！')
username = users[0]['UserName']

while True:
    try:
        send_info()
    except:
        pass
    time.sleep(1)
