import requests
from bs4 import BeautifulSoup
import re
import json
sesson = requests.Session()


import m3u8
class VideoDownload:
    def __init__(self):
        self.url = 'http://pc-shop.xiaoe-tech.com/appzDSBtscz6568/open/video.detail.get/1.0'
        self.headers = {
                   

                'Referer': 'http://pc-shop.xiaoe-tech.com/appzDSBtscz6568/video_details?id=v_59f19d6358caa_LC9iY6eT',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'http://pc-shop.xiaoe-tech.com',
                'Host': 'pc-shop.xiaoe-tech.com',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Accept-Language':'en-us',
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6',
                'Cookie': 'laravel_session=eyJpdiI6ImVwSnQyMG85NU1lamJPN2ErNysrd2c9PSIsInZhbHVlIjoiTmRDWk5RUEluZ1RGbXViRVN3aUhsN2pUMHR5NDBRd3FUaFQ3ZFlBbGJUOGo0UEpuTEVTcmRTM1VkTkd4Q2xWY3Y0SmowV0tvQmxmQW1GK09xXC9NQnRnPT0iLCJtYWMiOiJhNWM3MTBhNjJlNDNlMzM1MzY4N2RkNTBmZDkwNGZmMTBkNTFlZTY4MzJlNmFjZTgwOTk2YjRjYTJhMzgwMDFkIn0%3D; tgw_l7_route=1f4fc3a8216a1a6558ccfd82bd9a54b9',
                'Content-Length':'46',
                'X-Requested-With': 'XMLHttpRequest',
        }


        # self.login()
                
    def login(self):
        data = {
                'data[page_index]': '0',
                'data[page_size]': '10',
                'data[resource_id]': 'v_59f19d6358caa_LC9iY6eT',
                'data[resource_type]': '3',
            }
        response = sesson.post(self.url,data= data, headers=self.headers)
        if 'PC登录' not in response.text:
            print('登陆成功。')

            ff = json.loads(response.text)
            video_url  =  ff.get('data').get('video_hls')
            print(video_url)

            # response = sesson.get(video_url)
            # print(response.status_code)
            # with open('1.ts', 'wb') as code:
            #     code.write(response.content)

            return video_url
        else:
            print('登录失败！')



v = VideoDownload()

print(v.login())

def getM3u8(url):
    m3u8_obj = m3u8.load(url)  # this could also be an absolute filename

    ts_url_list = []

    base_uri = m3u8_obj.base_uri

    ts_list = m3u8_obj.files

    for _ts in ts_list:

        ts_url = base_uri + _ts

        ts_url_list.append(ts_url)

    # print ts_url

    # response = requests.head(ts_url)

    # if response.status_code == 200:
    #     print "URL 没问题"

    return ts_url_list



getM3u8(v.login())