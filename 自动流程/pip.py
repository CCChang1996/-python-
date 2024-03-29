# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:01:45 2019

@author: 13486
"""

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest


filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)

# 生成 FeatureUnion
features = []
features.append(('pca', PCA()))
features.append(('select_best', SelectKBest(k=6)))
# 生成 Pipeline
steps =[]
steps.append(('feature_union', FeatureUnion(features)))
steps.append(('logistic', LogisticRegression()))
model = Pipeline(steps)
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())