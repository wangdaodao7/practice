# -*- coding: utf-8 -*-

"""
    作者:     王导导
    版本:     1.0
    日期:     2018/02/11
    项目名称： 成绩数据分析
    项目参考地址：http://blog.csdn.net/qq_14959801/article/details/51382207

"""

import  matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np 
from PIL import Image
import pylab



custom_font = mpl.font_manager.FontProperties(fname = 'songti.ttf')

font_size = 10
fig_size = (8, 6)
bar_width = 0.35

name = ('小刚', '小芳')
subjects = ('物理', '化学', '生物')
scores = ((65, 80, 72), (70, 90, 85))

mpl.rcParams['font.size'] = font_size
mpl.rcParams['figure.figsize'] = fig_size

index = np.arange(len(scores[0]))

rects1 = plt.bar(index, scores[0],  bar_width, color='r')
rects2 = plt.bar(index+bar_width, scores[1], bar_width,color='g')
plt.ylim(ymax=100, ymin=0)

plt.title('成绩对比图',  fontproperties=custom_font)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=2, prop=custom_font)  
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom') 
        rect.set_edgecolor('white')
    
add_labels(rects1) 
add_labels(rects2) 
plt.show()

