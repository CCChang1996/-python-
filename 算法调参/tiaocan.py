# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:48:02 2019

@author: 13486
"""

from pandas import read_csv
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
model = Ridge()
#设置要遍历的参数
param_grid = {'alpha': [1, 0.1, 0.01, 0.001, 0]}
#通过网格搜索查询最优参数
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid.fit(X, Y)
print('最高得分： %.3f' % grid.best_score_)
print('最优参数： %s' % grid.best_estimator_.alpha)

#随机
#param_grid = {'alpha': uniform()}
#grid = RandomizedSearchCV(estimator=model, param_distributions=param_grid, n_iter=100, random_state=7)

