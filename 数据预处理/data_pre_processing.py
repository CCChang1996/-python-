# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 21:24:41 2019

@author: 13486
"""

from pandas import read_csv
from pandas import set_option
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer

filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
#调整数据尺度
transformer = MinMaxScaler(feature_range=(0,1))
#数据转换
newX = transformer.fit_transform(X)
#设定数据的打印格式
set_printoptions(precision=3)
#print(newX)


#正态化数据
transformer = StandardScaler().fit(X)
newX = transformer.transform(X)
set_printoptions(precision=3)
#print(newX)

#标准化数据
transformer = Normalizer().fit(X)
newX = transformer.transform(X)
set_printoptions(precision=3)
#print(newX)

#二值数据
transformer = Binarizer(threshold=0.0).fit(X)
newX = transformer.transform(X)
set_printoptions(precision=3)
print(newX)


