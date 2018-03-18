import requests
from bs4 import BeautifulSoup
import re



class VideoDownload:
    def __init__(self):
        self.url = 'http://pc-shop.xiaoe-tech.com/appzDSBtscz6568/video_details?id=v_59f19d6358caa_LC9iY6eT'
        self.headers = {
                    'Cookie': 'laravel_session=eyJpdiI6IjNIWE9VOVZ2K2lZTzNqSTA5VWc1bnc9PSIsInZhbHVlIjoicXhUVTdBTEVNUG1oZ0hHclg2bEFVbnFZR3FpNWYweTZ5M0VvaUVmV2p5OUN6UHg5d3gyNlppRzRGYmFjblJcL3YzZEJONWlRSU5BNE94XC9YV0owa285dz09IiwibWFjIjoiNmVkM2Q2MjBhZmM0MjcwZWYxY2RhZjY5ZTkwODAyNjExODRhOTFmOTE4OWYwMDkxYjgxZWU3NTJlYmZlOGUyOCJ9',
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6',
                    'Host': 'pc-shop.xiaoe-tech.com',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Connection': 'keep-alive',
                    'Accept-Language': 'en-us',
                    'Accept-Encoding': 'gzip, deflate',
                    'Upgrade-Insecure-Requests': '1'                
                    }

        self.headers2= {
                    'Accept-Encoding': 'gzip, deflate',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6',
                    'Host': 'vod2.xiaoe-tech.com',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Accept-Language': 'en-us',
                    'Referer': 'http://pc-shop.xiaoe-tech.com/appzDSBtscz6568/video_details?id=v_59f19d6358caa_LC9iY6eT',           
                    }



        self.headers3 ={
                    'Referer': 'http://pc-shop.xiaoe-tech.com/appzDSBtscz6568/video_details?id=v_59f19d6358caa_LC9iY6eT',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'http://pc-shop.xiaoe-tech.com',
                    'Host': 'pc-shop.xiaoe-tech.com',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Accept-Language': 'en-us',
                    'Accept-Encoding': 'gzip, deflate',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6',
                    'Cookie': 'laravel_session=eyJpdiI6IkVKREEzSSsxZkRDVnZqSjdFTldhMVE9PSIsInZhbHVlIjoiUm9SaVNoSzdEajRNVDU0VWRZV1B1UHBnN1JHcTlWMnFWT3BcLzZveUxDWFRETTFYZDRnZzVmTjdsaG1NSFRxdERTNzJub3NPd2twWnVLV3FCZWhTZllBPT0iLCJtYWMiOiJkMjM3Nzk4YzM4NDQ3NjU4NmRkZDZiZGE2NDM0NGMwN2I5OWY1ZGU2N2VmNWVmODA2ZWQ2Yzc5YTMyNDE3NjZmIn0%3D; tgw_l7_route=1f4fc3a8216a1a6558ccfd82bd9a54b9',
                    'Content-Length': '46',
                    'X-Requested-With': 'XMLHttpRequest'}
        self.login()
                
    def login(self):
        response = requests.get(self.url, headers=self.headers)
        if 'PC登录' not in response.text:
            print('登陆成功。')
        else:
            print('登录失败！')
    def get_v(self, v_url):
        # v_url = 'http://vod2.xiaoe-tech.com/9764a7a5vodtransgzp1252524126/7abb4d8b9031868223423997523/v.f230.ts?start=221328&end=271727&type=mpegts&t=5aac9b4d&us=770859&sign=599e53e44211322fece359f512f9911b'
        response = requests.get(v_url, headers=self.headers3)
        print('正在下载。')
        with open('1.ts', 'wb') as code:
            code.write(response.content)
        print(response)


 


# 'http://pc-shop.xiaoe-tech.com/appzDSBtscz6568/video_details?id=v_59f19d6358caa_LC9iY6eT'
        # 'http://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/7abb4d8b9031868223423997523/v.f20.mp4?start=0'
v = VideoDownload()
v.get_v('http://vod2.xiaoe-tech.com/9764a7a5vodtransgzp1252524126/7abb4d8b9031868223423997523/v.f230.m3u8?t=5aac9e27&us=260742&sign=0b67d7164e7d1ff50ada6daa06171b65')
