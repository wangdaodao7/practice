import datetime
import random
import time

import itchat
import lxml
import requests
from bs4 import BeautifulSoup

itchat.auto_login(hotReload=True)
# users = itchat.search_friends('杨欢')
# username = users[0]['UserName']
# print('登陆成功！！！')


def joke(num):
    url = 'https://www.qiushibaike.com/hot/page/{page}/'
    response = requests.get(url.format(page=num))
    soup = BeautifulSoup(response.text, 'lxml')
    txt = [txt.text.strip() for txt in soup.select('.content')]
    txt2 = random.choices(txt)
    return txt2[0]


# while True:
#     page = random.choices(range(1, 13))
#     msg = joke(page)
#     if len(msg) < 20:
#         page2 = random.choices(range(1, 13))
#         msg = joke(page2)
#         print(page2)
#     print(msg, page)
#     itchat.send('【笑话】{}'.format(msg), toUserName=username)

#     time.sleep(3)







msgs = ['小仙女，想你。现在是{min}:0{sec}，该第喝{num}杯水啦！',
        '最爱你的人温馨提示：现在是{min}:0{sec}，是时候喝{num}杯水啦！', '{min}:0{sec},喝第{num}杯水吧，我的小可爱！',
        '虽然有点像贴冷屁股，但是还是要大声说，亲爱的，{min}:0{sec}，第{num}杯水', '{min}:0{sec},第{num}杯水，了解一下']

msg_heshui = ['喝了没？', '赶紧去喝', '听我的话', '不喝我一直发，', '毛主席说，爱喝水的仙女才是好仙女']
msg_qilai = ['还在坐着吗', '别懒了，现在就起来吧',
             '小仙女，为了你的健康，还是啰嗦下，起来走走吧', '起来走俩步，小可爱', '起来走走，活到99']


def go():
    while True:
        now_hour = datetime.datetime.now().hour
        now_minute = datetime.datetime.now().minute
        now_second = datetime.datetime.now().second
        if now_second == 0:
            # itchat.send(random.choices(msgs)[0].format(min=now_hour, sec=now_minute,
                                                    #    num=now_hour - 8), toUserName=username)
            print('已发送')
            tt1 = random.choices(range(1, 5))[0]
            time.sleep(int(tt1))
            print(tt1, random.choices(msg_heshui)[0])
            # itchat.send(random.choices(msg_heshui)[0], toUserName=username)
            tt2 = random.choices(range(2, 7))[0]
            time.sleep(int(tt2))
            # itchat.send(random.choices(msg_qilai)[0], toUserName=username)
            print(tt2, random.choices(msg_qilai)[0])
        # if now_second == 30 and now_minute == 0:
        #     msg = joke(random.choices(range(1, 20)))
        #     if len(msg) < 20:
        #         msg = joke(random.choices(range(1, 20)))
        #     print(msg)
        #     itchat.send('【半小时笑话】{}'.format(msg), toUserName=username)
        time.sleep(1)
        print('{0}:{1}:{2}'.format(now_hour, now_minute, now_second))




# rooms = itchat.get_chatrooms(update=True)
rooms = itchat.search_chatrooms('表情包')

print(rooms[0])