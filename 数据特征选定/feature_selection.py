# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:05:53 2019

@author: 13486
"""
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.ensemble import ExtraTreesClassifier

filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
# 特征选定,卡方（chi-squared）选择四个对结果影响最大的数据特征
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)
set_printoptions(precision=3)
#print(fit.scores_)
features = fit.transform(X)
#print(features)

#通过递归消除来选定特征
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print("特征个数：")
print(fit.n_features_)
print("被选定的特征：")
print(fit.support_)
print("特征排名：")
print(fit.ranking_)

# 通过主要成分分析来选定数据特征
pca = PCA(n_components=3)
fit = pca.fit(X)
print("解释方差: %s" % fit.explained_variance_ratio_)
print(fit.components_)

#特征重要性
model = ExtraTreesClassifier()
fit = model.fit(X, Y)
print(fit.feature_importances_)