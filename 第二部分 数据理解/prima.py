# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 19:38:56 2019

@author: 13486
"""

from pandas import read_csv
#使用pandas导入csv数据
from pandas import set_option
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix


filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
#print(data.shape)
#print(data.dtypes)
#print(data.describe())

#set_option('display.width', 100)
#set_option('precision', 2)

#显示数据的相关性
#print(data.corr(method='pearson'))

#数据的分布分析
#print(data.skew())

#直方图
data.hist()
#plt.show()

#密度图
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
#plt.show()

#箱线图
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False)
#plt.show()

#相关矩阵图
correlations = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arrange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
#plt.show()

#散点矩阵图
scatter_matrix(data)
plt.show()

