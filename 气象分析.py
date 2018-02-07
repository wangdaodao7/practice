
import numpy as np
import pandas as pd
import datetime

import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from dateutil import parser

#加在数据为pd格式到内存中
#数据地址http://labfile.oss.aliyuncs.com/courses/780/WeatherData.zip

df_ferrara = pd.read_csv('ferrara_270615.csv')
df_mantova = pd.read_csv('mantova_270615.csv')
df_ravenna = pd.read_csv('ravenna_270615.csv')
df_torino = pd.read_csv('torino_270615.csv')
df_asti = pd.read_csv('asti_270615.csv')
df_bologna = pd.read_csv('bologna_270615.csv')
df_piacenza = pd.read_csv('piacenza_270615.csv')
df_cesena = pd.read_csv('cesena_270615.csv')
df_faenza = pd.read_csv('faenza_270615.csv')
df_milano = pd.read_csv('milano_270615.csv')

def work_one():
    y1 = df_ravenna['temp']
    x1 = df_ravenna['day']
    y2 = df_faenza['temp']
    x2 = df_faenza['day']
    y3 = df_cesena['temp']
    x3 = df_cesena['day']
    y4 = df_milano['temp']
    x4 = df_milano['day']
    y5 = df_asti['temp']
    x5 = df_asti['day']
    y6 = df_torino['temp']
    x6 = df_torino['day']

    # 日期数据转为datetime格式
    day_ravenna = [parser.parse(x) for x in x1]
    day_faenza = [parser.parse(x) for x in x2]
    day_cesena = [parser.parse(x) for x in x3]
    dat_milano = [parser.parse(x) for x in x4]
    day_asti = [parser.parse(x) for x in x5]
    day_torino = [parser.parse(x) for x in x6]

    #初始化图像
    fig, ax = plt.subplots()

    #设置横坐标轴的标签转动70°
    plt.xticks(rotation=70)
    #格式化时间格式
    hours = mdates.DateFormatter('%H:%M')
    #设置坐标轴的显示格式
    ax.xaxis.set_major_formatter(hours)
    #画图r为颜色
    ax.plot(day_ravenna,y1,'r',day_faenza,y2,'r',day_cesena,y3,'r')
    ax.plot(dat_milano,y4,'g',day_asti,y5,'g',day_torino,y6,'g')

    plt.show()



def work_two():
    dist = [df_ravenna['dist'][0],
        df_cesena['dist'][0],
        df_faenza['dist'][0],
        df_ferrara['dist'][0],
        df_bologna['dist'][0],
        df_mantova['dist'][0],
        df_piacenza['dist'][0],
        df_milano['dist'][0],
        df_asti['dist'][0],
        df_torino['dist'][0]
    ]

    temp_max = [df_ravenna['temp'].max(),
        df_cesena['temp'].max(),
        df_faenza['temp'].max(),
        df_ferrara['temp'].max(),
        df_bologna['temp'].max(),
        df_mantova['temp'].max(),
        df_piacenza['temp'].max(),
        df_milano['temp'].max(),
        df_asti['temp'].max(),
        df_torino['temp'].max()
    ]

    temp_min = [df_ravenna['temp'].min(),
        df_cesena['temp'].min(),
        df_faenza['temp'].min(),
        df_ferrara['temp'].min(),
        df_bologna['temp'].min(),
        df_mantova['temp'].min(),
        df_piacenza['temp'].min(),
        df_milano['temp'].min(),
        df_asti['temp'].min(),
        df_torino['temp'].min()
]

    fig, ax = plt.subplots()
    x1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    ax.plot(dist, temp_max ,'ro')
    plt.show()


work_two()