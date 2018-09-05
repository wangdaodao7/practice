# -*- coding: utf-8 -*-

"""
    作者:     王导导
    版本:     1.0
    日期:     2018/02/09
    项目名称：气象数据分析
    项目参考地址：http://blog.csdn.net/oxuzhenyi/article/details/68928892
"""

import numpy as np
import pandas as pd
import datetime
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser

# 加在数据为pd格式到内存中
# 数据地址http://labfile.oss.aliyuncs.com/courses/780/WeatherData.zip

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

    # 初始化图像
    fig, ax = plt.subplots()

    # 设置横坐标轴的标签转动70°
    plt.xticks(rotation=70)
    # 格式化时间格式
    hours = mdates.DateFormatter('%H:%M')
    # 设置坐标轴的显示格式
    ax.xaxis.set_major_formatter(hours)
    # 画图r为颜色
    ax.plot(day_ravenna, y1, 'r', day_faenza, y2, 'r', day_cesena, y3, 'r')
    ax.plot(dat_milano, y4, 'g', day_asti, y5, 'g', day_torino, y6, 'g')

    plt.show()


def work_two():

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
    ax.plot(dist, temp_max, 'ro')
    plt.show()




def work_three():
    dist1 = [[x] for x in dist[0: 5]]
    dist2 = [[x] for x in dist[5: 10]]

    temp_max1 = temp_max[0: 5]
    temp_max2 = temp_max[5: 10]

    svr_lin1 = SVR(kernel='linear', C=le3)
    svr_lin2 = SVR(kernel='linear', C=le3)

    svr_lin1.fit(dist1, temp_max1)
    svr_lin2.fit(dist2, temp_max2)

    xp1 = np.arange(10, 100, 10).reshape((9, 1))
    xp2 = np.arange(50, 100, 50).reshape((7, 1))
    yp1 = svr_lin1.predict(xp1)
    yp2 = svr_lin1.predict(xp2)

    ax.set_xlim(0, 400)
    ax.plot(xp1, yp1, c='b', label='2')
    ax.plot(xp2, yp2, c='g', label='1')
    plt.show()


work_two()









