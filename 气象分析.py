
import numpy as np
import pandas as pd
import datetime

import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from dateutil import parser

#加在数据为pd格式到内存中
#数据地址http://labfile.oss.aliyuncs.com/courses/780/WeatherData.zip

def work_one():
    df_milano = pd.read_csv('milano_270615.csv')
    y1 = df_milano['temp']
    x1 = df_milano['day']
    # 日期数据转为datetime格式
    day_milano = [parser.parse(x) for x in x1]
    #初始化图像
    fig, ax = plt.subplots()
    #设置横坐标轴的标签转动70°
    plt.xticks(rotation=70)
    #格式化时间格式
    hours = mdates.DateFormatter('%H:%M')
    #设置坐标轴的显示格式
    ax.xaxis.set_major_formatter(hours)
    #画图r为颜色
    ax.plot(day_milano, y1, 'r')
    plt.show()






work_one()
# df_ferrara = pd.read_csv('ferrara_270615.csv')
# df_mantova = pd.read_csv('mantova_270615.csv')
# df_ravenna = pd.read_csv('ravenna_270615.csv')
# df_torino = pd.read_csv('torino_270615.csv')
# df_asti = pd.read_csv('asti_270615.csv')
# df_bologna = pd.read_csv('bologna_270615.csv')
# df_piacenza = pd.read_csv('piacenza_270615.csv')
# df_cesena = pd.read_csv('cesena_270615.csv')
# df_faenza = pd.read_csv('faenza_270615.csv')




