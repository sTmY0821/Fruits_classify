import numpy as np
# 线性模型
import sklearn.linear_model as lm
# 模型性能评价模块
import sklearn.metrics as sm
import matplotlib.pyplot as mp
# 管线模块
import sklearn.pipeline as pl
import sklearn.preprocessing as sp

train_x, train_y = [], []
with open("../data/poly_sample.txt", 'rt') as f:
    for line in f.readlines():
        x, y = line.strip().split(',')
        train_x.append([float(x)])
        train_y.append(float(y))

train_x = np.array(train_x)
train_y = np.array(train_y)

# 创建模型
model = pl.make_pipeline(sp.PolynomialFeatures(3),lm.LinearRegression())

# 训练模型
model.fit(train_x, train_y)
# 预测
test_x = np.linspace(min(train_x), max(train_x), 1000)
pre_test_y = model.predict(test_x)
print(sm.r2_score(train_y, model.predict(train_x)))

mp.figure('Polynomial Regression', facecolor='lightgray')
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.title('Polynomial Regression', fontsize=20)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)
mp.scatter(train_x, train_y, c='dodgerblue', alpha=0.8, s=60, label='Sample')
mp.plot(test_x, pre_test_y, c='orangered', label='Pre')

mp.show()
