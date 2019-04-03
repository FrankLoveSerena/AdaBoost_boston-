#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# __author__ = 'Frank'
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error

# 加载数据
data = load_boston()
print(data.data)
# 分割数据
train_x, test_x, train_y, test_y = train_test_split(data.data, data.target, test_size = 0.25, random_state = 33)
# 使用AdaBoost回归模型
regressor = AdaBoostRegressor()
regressor.fit(train_x, train_y)
pred_y = regressor.predict(test_x)
mse = mean_squared_error(test_y, pred_y)
print('房价预测结果：', pred_y)
print('均方误差 = ', round(mse, 2))
